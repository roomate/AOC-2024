# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:00:58 2025

@author: hugon
"""



with open(r'C:\Users\hugon\OneDrive\Bureau\AOC\Day9\input.txt') as file:
    for l in file:
        line = l

class Block:
    def __init__(self, block_type, length, data):

        self.type = block_type #Tell if it is data(0) or void(1)
        
        self.length = length #size of void elements
        
        self.data = data #Numbers IDs in the data block

    def display(self):
        print('The Block data type is {}'.format(self.block_type))
        if self.block_type == 0:
            print('The Block data IDs are {}'.format(self.data))
        elif self.block_type == 1:
            print('The Block data length is {}'.format(self.length))

class Solution:
    def __init__(self, line):
        self.line = line
        self.nb_void = 0
        self.void_idx = []
        
        self.space_idx = []
        
    def parse_line(self):
        Blocks = []
        
        for id_, l in enumerate(self.line):
            if id_%2 == 0:
                self.space_idx += [len(Blocks)]
                block_file = Block(0, 0, [id_//2]*int(l))
                Blocks += [block_file]
            else:
                if int(l) > 0:
                    self.void_idx += [len(Blocks)]
                    block_void = Block(1, int(l), [])
                    self.nb_void += int(l)
                    Blocks += [block_void]
        return Blocks
        
    def partI(self):
        Blocks = self.parse_line()
        # self.display_block(Blocks)
        curr_void_id = self.void_idx.pop(0) #Id of the first void list to fill
        #Where the data is displaced from. At the first iteration, we know that 
        #it is a data type block.
        curr_block = Blocks.pop().data
        # print("Current data block is", curr_block)
        # print('\n')
        while self.nb_void != 0:
        #While you can fill some spaces
            if len(curr_block) == 0:
                #If it is simply a block of dots at the rightmost place
                if Blocks[-1].type == 1 and len(Blocks[-1].data) == 0:
                    self.nb_void -= Blocks[-1].length
                    Blocks.pop() #Remove the voids not preceding any data
                    self.void_idx.pop() #Remove the void ids, no figure will be placed here.
                    continue
                #This case can only happens at the end, when 
                elif Blocks[-1].type == 1 and len(Blocks[-1].data) != 0:
                    self.nb_void -= Blocks[-1].length
                    Blocks[-1].length = 0
                #If the last block is of data type
                if Blocks[-1].type == 0:
                    curr_block = Blocks.pop().data #If the last block is data type, take it.
                    
            #If the void block is full, it becomes a data type
            if Blocks[curr_void_id].length == 0:
                Blocks[curr_void_id].type = 0
                self.space_idx += [curr_void_id] #Add to the data space the filled block
                #Change of void block, take the first of the list
                try:
                    curr_void_id = self.void_idx.pop(0)
                except IndexError:
                    break
            self.nb_void -= 1
            Blocks[curr_void_id].data += [curr_block.pop()]
            Blocks[curr_void_id].length -= 1

        if len(curr_block) != 0:
            Blocks[-1].data += curr_block
        output = 0
        index = 0
        for i, block in enumerate(Blocks):
            for data in block.data:
                output += data*index
                index += 1
        return output

    def partII(self):
        Blocks = self.parse_line()
        for i, d in enumerate(self.space_idx[::-1]):
            curr_block_data = Blocks[d].data
            # self.display_block(Blocks)
            # print('\n')
            for void in self.void_idx: #Only the voids before the current data block
                if void < d:
                    curr_void_block = Blocks[void]
                    if curr_void_block.length >= len(curr_block_data):
                        curr_void_block.length -= len(curr_block_data)
                        curr_void_block.data += curr_block_data

                        #Change the block datatype
                        Blocks[d].type = 1
                        Blocks[d].length = len(curr_block_data)
                        Blocks[d].data = []

                        if curr_void_block.length == 0: 
                            curr_void_block.type = 0 #Do not place it into space_idx because you can change it
                            #only once
                            self.void_idx.remove(void)
                        break

        output = 0
        index = 0
        for i, block in enumerate(Blocks):
            for data in block.data:
                output += data*index
                index += 1
            index += block.length

        return output

    def display_block(self, Blocks):
        out = ''
        for i, block in enumerate(Blocks):
            for i in block.data:
                out += str(i)
            out += '.'*block.length
        print(out)
    
            
sol = Solution(line)
sol.partII()