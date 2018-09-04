###########################################
# Follow me 
# Sourabh Somani
# https://www.twitter.com/sourabh_somani
# https://www.facebook.com/hackersourabh
# sourabh_somani2010@hotmail.com
# Instagram : sourabhsomani8
###########################################

import datetime as date
from block import Block

def create_genesis_block():
  return Block(0, date.datetime.now(), "Genesis Block", 0)

def addBlock(last_block,data):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = data
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Adding Block
block_to_add = addBlock(blockchain[0],"A given money to B")
blockchain.append(block_to_add)

# Now do whatever you want?