# coding: UTF-8

from bourjois.models.database import *
from bourjois.models import *



if __name__ == '__main__':
    Base.metadata.create_all(engine)