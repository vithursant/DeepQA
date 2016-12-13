#!/usr/bin/env python3

# Copyright 2015 Conchylicultor. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
Load the cornell movie dialog corpus.

Available from here:
http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html

"""
import os
import tqdm
import multiprocessing
import time 

class CornellData:
    """

    """
    
    def __init__(self, dirName, corpus):
        """
        Args:
            dirName (string): directory where to load the corpus
        """
        self.lines = {}
        self.conversations = []

        #self.cores = cores
    
        MOVIE_LINES_FIELDS = ["lineID","characterID","movieID","character","text"]
        MOVIE_CONVERSATIONS_FIELDS = ["character1ID","character2ID","movieID","utteranceIDs"]
        
        #self.lines = self.loadLines(dirName + "movie_lines.txt", MOVIE_LINES_FIELDS)
        #self.conversations = self.loadConversations(dirName + "movie_conversations.txt", MOVIE_CONVERSATIONS_FIELDS)
        self.conversations = self.loadConversations(dirName + corpus, MOVIE_CONVERSATIONS_FIELDS)
        
        # TODO: Cleaner program (merge copy-paste) !!
        
    def loadLines(self, fileName, fields):
        """
        Args:
            fileName (str): file to load
            field (set<str>): fields to extract
        Return:
            dict<dict<str>>: the extracted fields for each line
        """
        lines = {}
        
        with open(fileName, 'r', encoding='iso-8859-1') as f:  # TODO: Solve Iso encoding pb !
            for line in f:
                values = line.split(" +++$+++ ")

                # Extract fields
                lineObj = {}
                for i, field in enumerate(fields):
                    lineObj[field] = values[i]
                
                lines[lineObj['lineID']] = lineObj

                #print ("Printing lines (loadLines): \n")
                #print (lines)       
                #exit()
        return lines
    '''
    def extractConversations(self, 
                                num_convos, 
                                id,
                                fp, 
                                file, 
                                conversations, 
                                collected_lines):
    '''
    '''
    def extractConversations(self, 
                                convos, 
                                file):
        conversations = []
        collected_lines = []

        for j in tqdm.tqdm(range(len(convos))):
        #for j in range(num_convos):
            #or line in fp:
            if "Start of Convo" in convos[j]:
                #print ("started at line", i)
                continue
            if "End of Convo" in convos[j]:
                #print ("end at line %s", convos[j])
                if(len(collected_lines) % 2 != 0):
                    collected_lines.pop()
        
                if (file == "switchboard.txt" or file == "watson_pii.txt"):
                    for i in range(0, len(collected_lines), 2):
                        collected_lines[i], collected_lines[i+1] = collected_lines[i+1], collected_lines[i] 
                
                conversations.append(collected_lines)
                break

            collected_lines.append(convos[j].strip())

    '''
    def make_dir(self):
        try:
            os.makedirs('./model')
        except OSError:
            pass 

    def loadConversations(self, fileName, fields):
        """
        Args:
            fileName (str): file to load
            field (set<str>): fields to extract
        Return:
            dict<dict<str>>: the extracted fields for each line
        """

        conversations = []
        collected_lines = []
        num_convos = 0;

        self.make_dir()

        with open(fileName,"r", encoding='iso-8859-1') as f:
            for line in f:
                if "Start of Convo" in line:
                    num_convos = num_convos + 1;

        with open(fileName, 'r', encoding='iso-8859-1') as fp:
            #all_lines = fp.readlines()
            #convos = fp.readlines()

            #for j in tqdm.tqdm(range(len(convos))):
            for j in tqdm.tqdm(range(num_convos)):
                for line in fp:
                    #if "Start of Convo" in convos[j]:
                    if "Start of Convo" in line:
                        #print ("started at line", i)
                        continue
                    #if "End of Convo" in convos[j]:
                    if "End of Convo" in line:
                        #print ("end at line", i)
                        if(len(collected_lines) % 2 != 0):
                            collected_lines.pop()
                
                        if (os.path.split(fileName)[1] == "switchboard.txt" or os.path.split(fileName)[1] == "watson_pii.txt"):
                            for i in range(0, len(collected_lines), 2):
                                collected_lines[i], collected_lines[i+1] = collected_lines[i+1], collected_lines[i]

                        conversations.append(collected_lines)
                        break
                        #break
                    #collected_lines.append(convos[j].strip())
                    collected_lines.append(line.strip())

            '''
            for i in range(0, procs):
                #conversations = list()
                collected_lines = list()
                process = multiprocessing.Process(target=self.extractConversations,
                                                    args=(num_convos, 
                                                            i, 
                                                            fp,
                                                            file,
                                                            self.conversations, 
                                                            collected_lines))
                jobs.append(process)

            for j in jobs:
                j.start()

            for j in jobs:
                j.join()
            '''
        #t1 = time.time()
        #total_n = t1-t0
        #print ("Conversations extractions complete: "),
        #print (total_n)
        #exit()
        #all_lines = fp.readlines()
        '''
        for j in tqdm.tqdm(range(num_convos)):
            for line in fp:
                if "Start of Convo" in line:
                    #print ("started at line", i)
                    continue
                if "End of Convo" in line:
                    #print ("end at line", i)
                    conversations.append(collected_lines)
                    break

                collected_lines.append(line.strip())

            if(len(collected_lines) % 2 != 0):
                collected_lines.pop()
            
            if (os.path.split(fileName)[1] == "switchboard.txt" or os.path.split(fileName)[1] == "watson_pii.txt"):
                for i in range(0, len(collected_lines), 2):
                    collected_lines[i], collected_lines[i+1] = collected_lines[i+1], collected_lines[i]
        '''
        #for convo in conversations:
        #    for sent in convo:
        #        print (sent)
        #exit()
        '''
        conversations = []
        with open(fileName, 'r', encoding='iso-8859-1') as f:  # TODO: Solve Iso encoding pb !
            for line in f:
                values = line.split(" +++$+++ ")
                
                # Extract fields
                convObj = {}
                for i, field in enumerate(fields):
                    convObj[field] = values[i]
                
                lineIds = convObj["utteranceIDs"][2:-3].split("', '")
                
                #print(convObj["utteranceIDs"])
                #for lineId in lineIds:
                    #print(lineId, end=' ')
                #print()
                    
                # Reassemble lines
                convObj["lines"] = []
                for lineId in lineIds:
                    convObj["lines"].append(self.lines[lineId])
                    
                conversations.append(convObj)

                #print ("Printing conversations: \n")
                #print (conversations)
                #exit()
        '''
        return conversations

    def getConversations(self):
        #print ("Hello")
        return self.conversations
