# Motaung Karabelo
# MTNKAR007
# CSC3002F
# OS_1-Assignment_1

from random import randint
import sys

#Function that implements the FIFO page replacement algorithm and returns the number of page faults that occur.
# parameters: 
            #size (int): The number of available page frames - can vary from 1 to 7
            #pages (list): A page reference string
# Returns:
            # Returns numbers of faults that the algorithm encounted
def FIFO(size, pages):
    queue = []                              # the queue is the FIFO algorithm
    fault = 0                               # records page faults
    for page in pages:                      # loop through an array of pages.
        if page not in queue:               # checks if the page is in memory
            fault += 1                      # if not, trap occurs and number of faults is incremented
            if len(queue) >= size:           # checks if the queue respects the frame size 
                queue.pop(0)                # removes the element in front of the array(First In, First Out)
            queue.append(page)              # appends to the back of the queue.
    return fault                            # return the number of faults found


# Function that implements the LRU (Least Recently Used) page replacement algorithm and returns the number of page faults that occur.
# parameters: 
            #size (int): The number of available page frames - can vary from 1 to 7
            #pages (list): A page reference string
# Returns:
            # Returns numbers of faults that the algorithm encounted
def LRU(size, pages):
    stack = []                   # stack, the page frames, is initially empty
    page_faults = 0              # tracks the number of page faults

    for page in pages:           # loops through each page in the memory
        if page not in stack:    # check if the page is in memory already
            page_faults += 1        # if not, a page fault has occurred
            if len(stack) >= size:  # check if there are no empty frames left
                del stack[size-1]       # remove the least recently used page
        else:                    # page is in memory
            stack.remove(page)      # remove page from old place in stack
        # put page on top of the stack because its the most recently used page.
        stack.insert(0, page)
    return page_faults

# Function that implements the optimal page replacement algorithm (OPT) and returns the number of page faults that occur.
# parameters: 
            #size (int): The number of available page frames - can vary from 1 to 7
            #pages (list): A page reference string
# Returns:
            # Returns numbers of faults that the algorithm encounted
def OPT(size, pages):
    memory = []                             # pages will be added to this list
    fault = 0                               # records page faults
    offset = 0                              # this variable will 
    pendingPages = []                       # pages still to used in the future
    for page in pages:
        pendingPages = pages[offset:]
        if page not in memory:              # check if the page is in memory already
            fault += 1                      # if not, a page fault has occurred
            
            if len(memory) < size:          # check if there are any free frames
                memory.append(page)         # if so, place page in a free frame
                #offset += 1
            else:
                                            # the frames are full, so we must replace the frame
                                            # that will not be used for the longest period of tim
                                            # using Optimal page Algorithm
                pendingPages = pages[offset:]
                pageToEvict = evictWhichPage(memory, pendingPages, size)

                # Swap pages 
                pos = memory.index(pageToEvict)
                memory.remove(pageToEvict)
                memory.insert(pos, page)
                #offset += 1                
        offset += 1                       # ignore the current page when we predict the future in the next iteration
    return fault


# Helper function for the OPT algorithm to find the the victim frame (frame to replace) i.e. the frame that will not be used for the longest time.
# Parameters:
        # frames (list): A list of the frames in memory
        # pages (list): A page reference string for future pages
# Returns:
        # The frame that will not be used for a while

def evictWhichPage(memory, pendingPages, size):
    stack = []                                    # stack data structure, element that will not be used for the longest time will be a the back of the array

    for page in memory:
        if page not in pendingPages:              # if page not upcoming, return the page 
            return page                           # Page will not be used in the future 
    for pPage in pendingPages:                    # loop through peonding pages(future)
        if pPage in memory and len(stack) < size: # keep the stack size to the size of memory, and check if page is in memory
            if pPage not in stack:                # Discard duplicates
                stack.append(pPage)
    return stack.pop()                            # remove the last page because it wont be used for a while


# Generates a random page-reference string of length N
# where page numbers range from 0 to 9
# Parameters: length (int): The desired length of the page reference string
# returns an array of elements between 0 and 9, of length (length)
def generateReferenceString(length):
    pages = []
    for i in range(length):
        pages.append(randint(0, 9))
    return pages


def main():
    refLength = int(input("Enter the length of the page reference string: "))
    # pages = [8,5,6,2,5,3,5,4,2,3,5,3,2,6,2,5,6,8,5,6,2,3,4,2,1,3,7,5,4,3,1,5]
    #pages = [8,5,6,2,5,3,5,4,2,3,5,3,2,6,2,5,6,8,5,6,2,3,4,2] # [8,5,6,2,5,3,5,4,2,3,5,3,2,6,2,5,6,8,5,6,2,3,4,2,1,3,7,5,4,3,1,5]
    # pages = "7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1".split(",")
    size = int(sys.argv[1])
    pages = generateReferenceString(refLength)
    print("Page reference string: ", pages)
    print("FIFO", FIFO(size, pages), "page faults")
    print("LRU", LRU(size, pages), "page faults")
    print("OPT", OPT(size, pages), "page faults")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: python paging.py [number of pages]")
    else:
        main()