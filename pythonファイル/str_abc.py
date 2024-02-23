from abc import *
#引数が必要なクラスはは必ずこのクラスを継承してください

class Str_Abc(ABC):

    @abstractmethod
    def __str__(self):
        pass