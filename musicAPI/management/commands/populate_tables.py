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
        parser.add_argument("filename", type=str, help="filename for csv file")

    def get_current_app_path(self):
        return apps.get_app_config("musicAPI").path

    def get_csv_file(self, filename):
        app_path = self.get_current_app_path()
        file_path = os.path.join(app_path, "management", "commands", filename)
        return file_path

    def clear_model(self, model_name):
        try:
            model_name.objects.all().delete()
        except Exception as e:
            raise CommandError(f"Error in clearing {model_name}: {str(e)}")

    def handle(self, *args, **kwargs):
        filename = kwargs["filename"]
        self.stdout.write(self.style.SUCCESS(f"filename:{filename}"))
        file_path = self.get_csv_file(filename)
        line_count = 0
        content_data = []
        try:
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";")
                for row in csv_reader:
                    if row != "" and line_count >= 1:
                        content_data.append(row)
                    line_count += 1

            singers = dict.fromkeys(set([x[0] for x in content_data]))
            songs = dict.fromkeys(set([x[1] for x in content_data]))
            albums = dict.fromkeys(set([(x[2], x[0]) for x in content_data]))

            self.clear_model(model_name=Singer)
            for key in singers.keys():
                try:
                    obj = Singer.objects.create(name=key)
                    singers[key] = obj.id
                except Exception as e:
                    raise CommandError(f"Error in inserting singer: {str(e)}")

            self.clear_model(model_name=Song)
            for key in songs.keys():
                try:
                    obj = Song.objects.create(title=key)
                    songs[key] = obj.id
                except Exception as e:
                    raise CommandError(f"Error in inserting song: {str(e)}")

            self.clear_model(model_name=Album)
            for key in albums.keys():
                try:
                    obj = Album.objects.create(
                        title=key[0], year=2023, singer=Singer.objects.get(name=key[1])
                    )
                    albums[key] = obj.id
                except Exception as e:
                    raise CommandError(f"Error in inserting album: {str(e)}")

            self.clear_model(model_name=Content)
            for el in content_data:
                try:
                    Content.objects.create(
                        song=Song.objects.get(title=el[1]),
                        album=Album.objects.get(title=el[2]),
                        track_number=el[3],
                    )

                except Exception as e:
                    raise CommandError(f"Error in inserting Content: {str(e)}")

        except FileNotFoundError:
            raise CommandError(f"File {file_path} does not exist")
