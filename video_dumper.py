import argparse
from pytubefix import YouTube
from pytube.helpers import safe_filename

'''
Use 10downloader.com to create a list with videos.
https://10downloader.com/playlist?v=https://www.youtube.com/@user_channel/videos&lang=en
Save the HTML to your computer.
Filter HTTP links from HTML to TXT.
Load TXT here. 
'''


def download_video(url_to_video, place_to_save):
    try: 
        you_tube_downloader = YouTube(url_to_video)
        you_tube_downloader = you_tube_downloader.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        file_name = f'{safe_filename(you_tube_downloader.title)}.mp4'
        you_tube_downloader.download(output_path=place_to_save, filename=file_name)
        print(f'FILENAME: [{file_name}]')
    except Exception as exception:
        print('_'*200)
        print(f'Error [{exception}]')
        print('_'*200)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download videos from a list and save them to a directory.")
    parser.add_argument("videos_txt", type=str, help="Path to the text file containing the list of videos.")
    parser.add_argument("save_directory", type=str, help="Path to the directory where the videos will be saved.")
    args = parser.parse_args()

    with open(args.videos_txt, 'r') as files:
        lines = files.readlines()
        i = 0
        for file in lines:
            file = file.strip()
            print('_'*200)
            i += 1
            print(f'{i} Downloading [{file}]')
            download_video(file, args.save_directory)
