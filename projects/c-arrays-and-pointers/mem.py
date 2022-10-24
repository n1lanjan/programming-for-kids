# creepy pasta code, just late afternoon hacking and smashing
import re
import random
import itertools
import time
import subprocess
import os

CARD=1
random.seed(7)


intro = [
"""                 ASCII

Computers understand only numbers, but
humans use sounds to communicate, so how
can computers and humans understand 
each other?

Humans have the alphabet, which is just
a way to have symbols representing a
sound, e.g. the symbol S represents the
sound you make that is similar to a 
snake. When you read the symbol S you 
know how it sounds. So now we I can
write something and you can read it even
though we have never met each other.

In 1963 some people gathered together
and put a number to most useful letters,
numbers, and symbols in the English 
alphabet, for example:
'0' is 48
'A' is 65
'B' is 66
'Z' is 90
'a' is 95
'z' is 122
'!' is 33
'?' is 63
...
This is called the ASCII Table. Its a 
letter to number table.
""",
"""          ASCII TABLE (partial)
CODE      CHAR            CODE   CHAR
000       NULL     |      033    !
010       \\n       |      ...
032       SPACE    |      ...
065       A        |      097    a
066       B        |      098    b
067       C        |      099    c
068       D        |      100    d
069       E        |      101    e
070       F        |      102    f
071       G        |      103    g
072       H        |      104    h
073       I        |      105    i
074       J        |      106    j
075       K        |      107    k
076       L        |      108    l
077       M        |      109    m
078       N        |      110    n
079       O        |      111    o
080       P        |      112    p
081       Q        |      113    q
082       R        |      114    r
083       S        |      115    s
084       T        |      116    t
085       U        |      117    u
086       V        |      118    v
087       W        |      119    w
088       X        |      120    x
089       Y        |      121    y
090       Z        |      122    z
""",

"""            CHARACTERS IN C
The character type in C needs one byte 
of memory.

[color:blue]char[/color] x = [color:brown]'a'[/color];
x = [color:brown]'b'[/color];
x = [color:teal]99[/color];

You can use [color:brown]'a'[/color] to get the ASCII value
of the character a (which is [color:teal]97[/color]). So
x = [color:brown]'a'[/color] means put [color:teal]97[/color] somewhere in memory
where we will store the value for the
variable x.

You can think of characters as one byte
numbers. By default they are signed,
so it can hold values from [color:teal]-128[/color] to [color:teal]127[/color].

For example:

x = [color:brown]'0'[/color] + [color:teal]17[/color];

Means, take the ASCII value of [color:brown]0[/color], which
is [color:teal]48[/color] and add [color:teal]17[/color] to it, so the variable x
will store the value [color:teal]65[/color], which is [color:brown]'A'[/color].
So if we do printf("%c",x) it will
print [color:brown]'A'[/color]. 

Use %c to print the character value of 
an ASCII code.
""",
"""            ARRAYS IN C
Array is a continuous piece of memory,
where each element has the same size.
For example array of 5 integers:

[color:blue]int[/color] a[color:teal][5][/color];

Each integer is 4 bytes, so 20 bytes
will be needed (5 elements * 4 bytes).

Array of characters is easier to think
about, because each character is exactly
1 byte:

[color:blue]char[/color] a[color:teal][5][/color];

So we will need 5 * 1 byte of continuous 
memory. The value of the array variable
is actually just the memory address of
the first element of the array.
Lets imagine it is on address 199932.

To access the elements we do:
[color:purple]a[0] = 48;[/color]
[color:red]a[3] = 49;[/color]
...
Which you can read as:
MEMORY AT ADDR [color:purple]199932+0*1 = 48[/color]
MEMORY AT ADDR [color:red]199932+3*1 = 49[/color]
We multiplty by 1 because each [color:blue]char[/color] is 1
byte, for [color:blue]int[/color] we need to multiply by 4.
""",
"""            POINTERS IN C

[color:blue]char[/color] x = [color:brown]'a'[/color];

There is some place in memory holding
the value [color:teal]97[/color] (the ASCII code for [color:brown]'a'[/color]).
Lets imagine its on memory address [color:red]251[/color]

To modify the value of x you can do:

x = [color:brown]'b'[/color];

Now on address [color:red]251[/color] we have 98, ASCII
for [color:brown]'b'[/color]. You can get the address of x
you use & like so:

[color:blue]char[/color] *p;
p = &x;

that means, make a variable p that will 
be a pointer to char, and later we 
assign it the value of the address of x, 
so the actual value of p will be [color:red]251[/color].

Now we can use p to modify x:
[color:red]*p = 'c'[/color], will go to address [color:red]251[/color] and 
put [color:teil]99[/color] there, the [color:red]*p[/color] means: follow the 
pointer of p, or 'dereference' p.

printf("%c",x) will print 'c'
Remember p is just a number!
""",
"""            STRINGS IN C
String is a continuous sequence of 
characters. C does not have a string
type, so strings are just arrays of
characters that end with 0.

[color:blue]char[/color] a[color:teal][3][/color] = [color:teal]{[/color][color:brown]'h'[/color], [color:brown]'i'[/color], [color:teal]0}[/color];
[color:blue]char[/color] b[color:teal][3][/color] = [color:teal]{104, 105, 0}[/color];
[color:blue]char[/color] *c = [color:brown]"hi"[/color];

Those three represent the same thing.

The value of the variable is actually
a pointer to the first element of the
string.

[color:blue]char[/color] v = c[color:teal][1][/color]
[color:blue]char[/color] v = *[color:teal]([/color]c + [color:teal]1)[/color]

both do the same, means go to wherever
address c holds, and add 1 to it and follow.
This is called dereferencing, or 
following a pointer.

To print strings use the %s formatting:
printf("%s",a);
printf("%s",b);
printf("%s",c);
%s will just start from the address of
the variable, and go forward until it
reaches value of 0.

""",
"""


                 RULES:


1. Split the code cards amongst the 
   players.

2. Put the memory cards face down on
   the table.

3. Pick the top memory card, 
   and put it face up in the middle of 
   the table.

4. Find a code card matching the memory.
   All variables have to have the correct
   value in the memory card.

5. First player that finds a match
   wins the round.

6. GOTO 3


""",
"""                 HISTORY

C was made in the '70s, so about 50 
years ago, by the titans Dennis Richie,
Ken Thompson, Brian Kernighan an others.

It is still one of the most used langu-
ages today.

It has extremely simple syntax:
[color:magenta]auto,break,case,char,const,continue,[/color]
[color:magenta]default,do,double,else,enum,extern,float[/color]
[color:magenta]for,goto,if,int,long,register,return,[/color]
[color:magenta]short,signed,sizeof,static,struct,switch,[/color]
[color:magenta]typedef,union,unsigned,void,volatile,[/color]
[color:magenta]while.[/color]

Those are all of its keywords.

Simple syntax does not mean simple lan-
guage. It takes extreme discipline to
write portable, robust and resilient C
code. And yet, most of the usable
programs are written in C or interact
with it somehow.

C is an invented language, it is not
discovered like LISP, and it is invented
in such a way, that makes it easy to 
program the computers we made, and it
does that very well.
""",
]
for c in intro:
    print(f"CARD:{CARD}")
    CARD+=1
    print(c)
    

code = [
"""
char name[6] = {'j', 'a', 0, 0, 's', 0}; // PY: x
name[2] = 'c';
name[3] = 'k';

printf("%s\\n",name);
""",
"""
char *world = "hello world"; // PY: x

printf("%s\\n",world);
""",
"""
char word[] = {'h', 'i', '!', 0}; // PY: x

printf("%s\\n",word);
""",

"""
char *alphabet = malloc(10); // PY: x

for (int i = 0; i < 9; i++) {
    *(alphabet + i) = 65 + i;
}
alphabet[9] = 0;

printf("%s\\n",alphabet);
""",
"""
char cow[4]; // PY: x

cow[0] = 'm';
*(cow+1) = 'o';
cow[2] = 'o';
cow[3] = 0;

printf("%s\\n",cow);
""",
"""
char foo[4]; // PY: x

0[foo] = 'b';
foo[1] = 'a';
(1+1)[foo] = 'r';
foo[1+2] = 0;

printf("%s\\n",foo);
""",

"""
char year[5]; // PY: x

year[0] = '1';
year[1] = '9';
year[2] = '7';
year[3] = '2';
year[4] = 0;

printf("%s\\n",year);
""",
"""
char year[5]; // PY: x

year[0] = 49;
year[1] = 57;
year[2] = 55;
year[3] = 50;
year[4] = 0;

printf("%s\\n",year);
""",

"""
char zeroToNine[11]; // PY: x

zeroToNine[0] = 48;
for (int i = 1; i < 10; i++) {
    zeroToNine[i] = zeroToNine[0] + i;
}
zeroToNine[10] = 0;

printf("%s\\n",zeroToNine);
""",

"""
char *hello = "world"; // PY: x
char *p = hello + 2; // PY: x + 2

printf("%s\\n",p);
printf("%s\\n",hello);
""",


"""
char hello[5] = {'h', 'e', 'y', 'o', 0}; // PY: x
char *p = hello + 1; // PY: x + 1

printf("%s\\n",p);
printf("%s\\n",hello);
""",


"""
char *hello = "hello world"; // PY: x
char *pa = hello + 4; // PY: x + 4
char *pb = pa + 2; // PY: x + 6

printf("%s\\n",pa);
printf("%s\\n",pb);
printf("%s\\n",hello);
""",
    
"""
char *hello = "hello world"; // PY: x
char *pa = hello + 4; // PY: x + 4
char *pb = pa - 3; // PY: x + 1

printf("%s\\n",pa);
printf("%s\\n",pb);
printf("%s\\n",hello);
""",


"""
char *hello = "hello world"; // PY: x
char *pa = &hello[5]; // PY: x + 5
char *pb = pa - 5; 

pb = pb + 6; // PY: x + 6

printf("%s\\n",pa);
printf("%s\\n",pb);
printf("%s\\n",hello);
""",

"""
char *hello = "hello world"; // PY: x
char *pa = &hello[0]; // PY: x
char *pb = pa + 6; // PY: x + 6

printf("%s\\n",pa);
printf("%s\\n",pb);
printf("%s\\n",hello);
""",

"""
char *hello = "hello world"; // PY: x
char *pa = &hello[0]; // PY: x
char *pb = &pa[6]; // PY: x+6

printf("%s\\n",pa);
printf("%s\\n",pb);
printf("%s\\n",hello);
""",


"""
char *cow = "moo"; // PY: x
char *pa = &cow[0]; // PY: x

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char *cow = "moo"; // PY: x
char *pa = &cow[2]; // PY: x + 2

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char *cow = "moo"; // PY: x
char *pa = &cow[1]; // PY: x + 1

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char *cow = "moo"; // PY: x
char *pa = cow; // PY: x

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char *cow = "moo"; // PY: x
char *pa = cow + 1 - 1; // PY: x

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char cow[4] = {'m', 'o', 'o', 0}; // PY: x
char *pa = cow + 1; // PY: x+1

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char cow[4] = {'m', 'o', 'o', 0}; // PY: x
char *pa = cow + 2; // PY: x+2

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
]


random.shuffle(code)
codeCycle = itertools.cycle(code)

runCode = {}
for i in range(len(code) + 1):
    mem = [(0,'zero')]*256
    seen={}
    for c in [next(codeCycle),next(codeCycle), next(codeCycle), next(codeCycle)]:

        program = """
    #include <stdio.h>
    #include <stdlib.h>
    
    int main(void) {
        """ + c + """
        return 0;
    }
    """
        with open("current.c","w") as f:
            f.write(program)
    
        output = subprocess.getoutput("gcc -o current current.c")
        if output.strip() != '':
            print(output);
            os.exit(1)
    
        # append it to memory
        w = subprocess.getoutput("./current").rstrip()
        runCode[c] = w

        splitted = w.split("\n")
        if len(splitted) != 1:
            w = splitted[1] # use only the whole string

        pointers = []
        for line in c.split("\n"):
            if "PY:" in line:
                a,b = line.split("PY:")
                pointers.append(b)

        while True:
            offset = random.randint(0, len(mem) - len(w) - 1 - len(pointers) - 2)
            if w in seen:
                offset = seen[w]
            else:
                busy = False
                for j in range(len(w)+2):
                    if mem[j + offset][1] != 'zero':
                        busy = True
        
                if busy:
                    continue
    
    
                for j in range(len(w)):
                    v = ord(w[j])
                    mem[j + offset] = (v,'value')
                mem[len(w) + offset] = (0,'value')                
            # used by the eval
            x = offset
            for p in pointers:
                v = eval(p)

                while True:
                    r = random.randint(1, len(mem)-4)
                    if mem[r-2][1] == 'zero' and mem[r-1][1] == 'zero'  and mem[r][1] == 'zero' and mem[r+1][1] == 'zero' and mem[r+2][1] == 'zero':
                        mem[r] = (v,'pointer')
                        break

            seen[w] = offset                
            break

      
    print(f'CARD:{CARD}')
    CARD+=1
    c = ''
    for i in range(32):
        print(f"{(i*8):3} | ", end='')
        
        if c != '':
            print(f"[color:{c}]",end='')
        for j in range(8):
            v,kind = mem[(i * 8) + j]
            if kind != 'zero':
                if c == '':
                    c = 'red'
                    if kind == 'pointer':
                         c = 'blue'
                    print(f"[color:{c}]",end='')
            else:
                if c != '':
                    c = ''
                    print(f"[/color]", end='')                
            print(f"{v:03} ",end='')
        if c != '':
            print(f"[/color]")
        else:
            print()
        

def colorme(s, color):
    out = []
    for l in s.splitlines():
        out.append(f"[color:{color}]{l}[/color]")
    return "\n".join(out)

for c in runCode:
    print(f'CARD:{CARD}')
    CARD+=1

    prints = runCode[c]
    comment = colorme(f"/*\nprints:\n{prints}\n*/", 'green')
    c = re.sub(r'(\[|\])','[color:teal]\\1[/color]',c)
    c = re.sub(r'(\(|\))','[color:teal]\\1[/color]',c)
    c = re.sub(r'(\{|\})','[color:teal]\\1[/color]',c)

    c = re.sub('(char|int\s+)','[color:blue]\\1[/color]',c)
    c = re.sub('(for)','[color:magenta]\\1[/color]',c)
    c = re.sub(r"(?<!')(\d+)",'[color:teal]\\1[/color]',c)
    c = re.sub('printf','[color:olive]printf[/color]',c)


    c = re.sub(r'(".*?")','[color:brown]\\1[/color]',c)
    c = re.sub(r'(\'.*?\')','[color:brown]\\1[/color]',c)


    c = f"{c}\n{comment}"
    n = int((32/2)) - int((len(c.split('\n'))) / 2) - 1
    print('\n' * n)
    

    for l in c.split('\n'):
        l = re.sub(r"//.*PY: .*","", l)
        print(l)
    print("")

    
