###########################################
# Follow me 
# Sourabh Somani
# https://www.twitter.com/sourabh_somani
# https://www.facebook.com/hackersourabh
# sourabh_somani2010@hotmail.com
# Instagram : sourabhsomani8
###########################################

import hashlib as hasher

class Block:
  def __init__(self,index,data,timestamp,previoushash):
    self.index=index
    self.data=data
    self.timestamp=timestamp,
    self.previoushash=previoushash

    self.hash=self.hashBlock()

  def hashBlock(self):
    sha=hasher.sha256()
    sha.update((str(self.index)+str(self.data)+str(self.timestamp)+str(self.previoushash)).encode('utf-8'))
    return sha.hexdigest()