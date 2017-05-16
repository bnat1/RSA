Contents of this submission

keypair.txt:
	contains the public and private key pair generated from the program, in the format of (exponent, modulus) for each of them. 

message.txt:
	contains a message signed with the private key found in keypair.txt

src:
	directory holding the python program, keygen.py

Instructions for Running Program:
In the src directory, type in "python keygen.py <modulus size>", where <modulus size> is the length of the modulus in bits, hit return to run the program. For example for a modulus size of 2048, use the command:	python keygen.py 2048