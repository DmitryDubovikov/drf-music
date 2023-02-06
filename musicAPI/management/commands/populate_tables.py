from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
import os

from musicAPI.models import Singer, Song, Album, Content


class Command(BaseCommand):
    help = "populates tables"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument("dirname", type=str, help="dirname for csv files")

    def get_current_app_path(self):
        return apps.get_app_config("musicAPI").path

    def get_csv_files(self, dirname):
        app_path = self.get_current_app_path()
        file_paths = []
        file_paths.append(os.path.join(app_path, dirname, "Singers.csv"))
        file_paths.append(os.path.join(app_path, dirname, "Songs.csv"))
        file_paths.append(os.path.join(app_path, dirname, "Albums.csv"))
        file_paths.append(os.path.join(app_path, dirname, "Content.csv"))
        return file_paths

    def clear_model(self, model_name):
        try:
            model_name.objects.all().delete()
        except Exception as e:
            raise CommandError(f"Error in clearing {model_name}: {str(e)}")

    def handle(self, *args, **kwargs):
        dirname = kwargs["dirname"]
        file_paths = self.get_csv_files(dirname)

        for file_path in file_paths:
            model_data = []
            model_fields = []
            line_count = 0

            try:
                with open(file_path) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=";")
                    for row in csv_reader:
                        if line_count == 0:
                            model_fields = row.copy()
                        if row != "" and line_count >= 1:
                            el = {}
                            for i in range(len(row)):
                                el[model_fields[i]] = row[i]
                            model_data.append(el)
                        line_count += 1

                    if file_path.find("Singer") != -1:
                        django_list = [Singer(**vals) for vals in model_data]
                        self.clear_model(model_name=Singer)
                        Singer.objects.bulk_create(django_list)

                    elif file_path.find("Song") != -1:
                        django_list = [Song(**vals) for vals in model_data]
                        self.clear_model(model_name=Song)
                        Song.objects.bulk_create(django_list)

                    elif file_path.find("Album") != -1:
                        for el in model_data:
                            singer = Singer.objects.get_or_create(name=el["singer"])[0]
                            el["singer"] = singer
                        django_list = [Album(**vals) for vals in model_data]
                        self.clear_model(model_name=Album)
                        Album.objects.bulk_create(django_list)

                    elif file_path.find("Content") != -1:
                        for el in model_data:
                            song = Song.objects.get_or_create(title=el["song"])[0]
                            el["song"] = song
                            album = Album.objects.get_or_create(title=el["album"])[0]
                            el["album"] = album
                        django_list = [Content(**vals) for vals in model_data]
                        self.clear_model(model_name=Content)
                        Content.objects.bulk_create(django_list)

            except FileNotFoundError:
                raise CommandError(f"File {file_path} does not exist")
