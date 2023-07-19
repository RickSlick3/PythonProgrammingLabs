# importing the multiprocessing module
import multiprocessing
import os

def sqrR(n):
    # square root calculator
	print("Square root of {0}: {1:.5f}".format(int(n), pow(n,(1/2))))

def cubeR(n):
	# cube root calculator
	print("Cube root of {0}: {1:.5f}".format(int(n), pow(n,(1/3))))

def fourthR(n):
    # fourth root calculator
    print("Fourth root of {0}: {1:.5f}".format(int(n), pow(n,(1/4))))

if __name__ == "__main__":
    
    # user gets to choose N
    n = float(input("Enter a number n: "))

    # creating processes
    p1 = multiprocessing.Process(target = sqrR, args=(n, ))
    p2 = multiprocessing.Process(target = cubeR, args=(n, ))
    p3 = multiprocessing.Process(target = fourthR, args=(n, ))

    # starting processes
    p1.start()
    p2.start()
    p3.start()
    
    print("\nProof that each process uses a different processor:")
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))
    print("ID of process p1: {}".format(p3.pid))
    
    # checking processes
    print("\nProcess p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))
    print("Process p3 is alive: {}\n".format(p3.is_alive()))
        
    # wait until processes are finished
    p1.join()
    p2.join()
    p3.join()

    # both processes finished
    print("\nAll 3 processes finished execution:")

    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))
    print("Process p3 is alive: {}".format(p3.is_alive()))