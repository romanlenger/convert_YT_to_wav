from pytube import YouTube
from pydub import AudioSegment
import os


def convert(link):
    yt = YouTube(link, use_oauth=True)
    streams = yt.streams.get_by_itag(251)
    file_path = streams.download(output_path='results')

    audio = AudioSegment.from_file(file_path, format="webm")
    wav_path = os.path.splitext(file_path)[0] + '.wav'
        
    audio.export(wav_path, format="wav")
    os.remove(file_path)
    
    return wav_path


if __name__ == '__main__':
    URL = input('Link: ')
    convert(URL)