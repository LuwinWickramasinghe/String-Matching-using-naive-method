def dotsearch(txt,pat):
    n = len(txt)
    m = len(pat)-1

    i = 0
    while i < n - m + 1:
        j = 0
        while (j < m and (txt[i + j] == pat[j] or pat[j] == '.')):
            j += 1
        if (j == m):
            with open('output.txt','a') as file:
                 file.write("Pattern found at index ")
                 file.write(str(i))
                 file.write("\n")

            i += j  # Move past the matched pattern

        else:
            i += 1

def asterisksearch(txt, pat):
    n = len(txt)
    m = len(pat) - 1

    for i in range(n - m + 1):
        j = 0
        while j < m and (txt[i + j] == pat[j] or pat[j] == '*' or pat[j+1] == '*'):
            j += 1
        if j == m:
            with open('output.txt','a') as file:
                 file.write("Pattern found at index ")
                 file.write(str(i))
                 file.write("\n")

            i += j
        else:
            i += 1
      
def plussearch(txt, pat):

    n = len(txt)
    m = len(pat)-1
    
    i = 0
    while i < n - m + 1:
        j = 0
        while j < m and (txt[i + j] == pat[j] or pat[j] == '+'):
            j += 1
        if j == m:
            with open('output.txt','a') as file:
                 file.write("Pattern found at index ")
                 file.write(str(i))
                 file.write("\n")

            i += j  # Move past the matched pattern

        else:
            i += 1
     
def Qsearch(txt, pat):
    n = len(txt)
    m = len(pat)-1

    for k in range(len(pat)):
        if pat[k] == '?':
            index_of_q = k
            break  # Stop searching after finding the first '?'

    part1 = pat[:index_of_q]
    part2 = pat[index_of_q + 1:]  # Skipping the ? an concatinate
    new_pattern1 = part1 + part2

    part3 = pat[:index_of_q-1]
    part4 = pat[index_of_q + 1:]  
    new_pattern2 = part3 + part4
    print(new_pattern1 , new_pattern2)

    for r in range(n - m):
        l = 0
        while (l < m-1 and (txt[r + l] == new_pattern2[l])):
            l += 1
        if (l == m-1):
            with open('output.txt','a') as file:
                 file.write("Pattern found at index ")
                 file.write(str(r))
                 file.write("\n")


    for i in range(n - m + 1):
        j = 0
        while (j < m and (txt[i + j] == new_pattern1[j])):
            j += 1
        if (j == m):
            with open('output.txt','a') as file:
                 file.write("Pattern found at index ")
                 file.write(str(i))
                 file.write("\n")


     
     
def pattern_search(String, Pattern):
    

    if '.' in Pattern:
        dotsearch(String, Pattern)

    elif '*' in Pattern:
        asterisksearch(String, Pattern)

    elif '+' in Pattern:
        plussearch(String, Pattern)

    elif '?' in Pattern:
        Qsearch(String, Pattern)
    
    else:
        naive_search(String, Pattern)


def naive_search(txt, pattern):
	M = len(pattern)
	N = len(txt)
    

	# A loop to slide pattern[] one by one */
	for i in range(N - M + 1):
		j = 0

		while(j < M):
			if (txt[i + j] != pattern[j]):
				break
			j += 1

		if (j == M):
                     with open('output.txt','a') as file:
                        file.write("Pattern found at index ")
                        file.write(str(i))
                        file.write("\n")
             

# Main Drive Code
if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        content = file.read()
        #print(content)

    with open('pattern.txt', 'r') as file:
        pattern = file.read()

    pattern_search(content , pattern)