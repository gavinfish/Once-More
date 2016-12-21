import os.path

from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence


class Audio():
    SUPPORT_TYPE = ['mp3', 'wav']

    def __init__(self):
        self.name = None
        self.type = None
        self.audio = None
        self.audioChunks = []
        self.audioCount = 0
        self.__index = 0

    def load(self, fullFileName):
        fileName = fullFileName.split(os.path.sep)[-1]
        self.name = fileName.split(".")[0]
        self.type = fileName.split(".")[-1]

        if self.type not in Audio.SUPPORT_TYPE:
            raise EnvironmentError("not support " + self.type)

        self.audio = AudioSegment.from_file(fileName, self.type)

    def slice(self, minSilenceLen=1000, silenceThresh=-30):
        self.audioChunks = split_on_silence(self.audio, min_silence_len=minSilenceLen, silence_thresh=silenceThresh)
        self.audioCount = len(self.audioChunks)

    def __dump(self, path=''):
        for i, chunk in enumerate(self.audioChunks):
            outFile = os.path.abspath('.') + os.path.sep + path + os.path.sep + self.name + str(i) + "." + self.type
            chunk.export(outFile, format=self.type)

    def previewSlice(self):
        if self.__index > 0:
            self.__index -= 1

    def nextSlice(self):
        if self.__index < self.audioCount - 1:
            self.__index += 1

    def playSlice(self):
        play(self.audioChunks[self.__index])
