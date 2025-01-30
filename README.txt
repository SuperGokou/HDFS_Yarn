Ming Xia
ID:11399343



Steps Run the program:

---> Install and setup the hadoop

	1. hadoop jar hadoop-streaming-3.3.1.jar -input input -output output  
	2. cat part-00000 |python3 mapper.py|sort -k1,1|python3 reducer.py > outputfile.txt
	3. cat part-00000 |python3 mapper.py|sort|python3 reducer.py > outfile.txt


