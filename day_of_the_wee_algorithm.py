# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:21:55 2019

@author: User
"""
"""Here is a formula for finding the day of the week for ANY date. 

   N = d + 2m + [3(m+1)/5] + y + [y/4] - [y/100] + [y/400] + 2

where d is the number or the day of the month, m is the number of the 
month, and y is the year. The brackets around the divisions mean to 
drop the remainder and just use the integer part that you get.

Also, a VERY IMPORTANT RULE is the number to use for the months for 
January and February. The numbers of these months are 13 and 14 of the 
PREVIOUS YEAR. This means that to find the day of the week of New 
Year's Day this year, 1/1/98, you must use the date 13/1/97. (It 
sounds complicated, but I will do a couple of examples for you.)

After you find the number N, divide it by 7, and the REMAINDER of that 
division tells you the day of the week; 1 = Sunday, 2 = Monday, 3 = 
Tuesday, etc; BUT, if the remainder is 0, then the day is Saturday, 
that is: 0 = Saturday.

As an example, let's check it out on today's date, 3/18/98. Plugging 
the numbers into the formula, we get;

   N = 18 + 2(3) + [3(3+1)/5] + 1998 + [1998/4] - [1998/100]
       + [1998/400] + 2

So doing the calculations, (remember to drop the remainder for the 
divisions that are in the brackets) we get;

   N = 18 + 6 + 2 + 1998 + 499 - 19 + 4 + 2 = 2510

Now divide 1510 by 7 and you will get 358 with a remainder of 4. Since 
4 corresponds to Wednesday, then today must be Wednesday. 

You asked about New Year's Day, so let's look at this year, 1/1/98. 
Because of the "Very Important Rule," we must use the "date" 13/1/97 
to find New Year's Day this year. Plugging into the formula, we get;

   N = 1 + 2(13) + [3(13+1)/5] + 1997 + [1997/4] - [1997/100]
       + [1997/400] + 2

   N = 1+ 26 + 8 + 1997 + 499 - 19 + 4 + 2 = 2518

Now divide 2518 by 7 and look at the remainder: 2518/7 = 359 with a 
remainder of 5. Since 5 corresponds to Thursday, New Year's Day this 
year was on a Thursday.

This is a very enjoyable formula, I hope you have fun with it.


The two different formula for finding the day in the weak is

 1. f = k + [(13*m-1)/5] + D + [D/4] + [C/4] - 2*C


 2.  N = d + 2m + [3(m+1)/5] + y + [y/4] - [y/100] + [y/400] + 2

Obviously these two formulas are equivalent, but I can't see why.  
Why the 2m? Why the +2?  Could you be so kind as to explain this
equivalence?  I guess I'm trying to understand why the formula works; 
what is the underlying idea. The 2m and the +2 throw me.

Thanks.  Jim
Date: 08/26/2002 at 22:33:56
From: Doctor Peterson
Subject: Re: Zeller's congruence

Hi, Jim.

The first thing to do is to note the differences:

In the FAQ,

    f = k + [(13*m-1)/5] + D + [D/4] + [C/4] - 2*C

    "m" is the month number starting with March as 1;
    "k" is the day of the month;
    the year is given by C, the century, and D, the last two digits;
    in the result, 0 means Sunday.

In the alternative formula, 

    N = d + 2m + [3(m+1)/5] + y + [y/4] - [y/100] + [y/400] + 2

    "m" is the month number starting with January as 1;
    "y" is the year;
    in the result 0 means Saturday.

So if we try to write the latter using the variables of the former, we
will have to replace

    d with k
    m with m+2 (so March is 3)
    y with 100C+D
    and subtract 1 from N to get f (so Sunday is 0).

We get

    f = N-1 

      =   k + 2(m+2) + [3((m+2)+1)/5] + (100C+D) + [(100C+D)/4]
        - [(100C+D)/100] + [(100C+D)/400] + 2 - 1

      =   k + 2m + 4 + [3(m+3)/5] + 100C + D + [25C + D/4]
        - [C + D/100] + [C/4 + D/400] + 1

      =   k + 2m + 4 + [3m/5 + 9/5] + 100C + D + 25C + [D/4]
        - C - 0 + [C/4] + 0 + 1

      =   k + [10m/5 + 4 + 3m/5 + 9/5 + 1] + 124C + D + [D/4] + [C/4]

      =   k + [(13m + 4)/5 + 6] + D + [D/4] + [C/4] + 124C

      =   k + [(13m-1)/5 + 7] + D + [D/4] + [C/4] + 124C

This isn't quite right, is it? Unless 

  7 + 124C = -2C, 

it can't be the same.

Ah! I realized what we're missing when I tried checking this by doing 
each calculation for a specific date: the answer is not this whole 
expression, but the remainder when we divide by 7. The two forms will 
be the same if

    7 + 124C = -2C (mod 7).

And since 124 = 7*17 + 5 = 7*18 - 2, it is in fact true that the 
remainder of the left side, 7*(1+18C) - 2C, will be the same as the 
remainder of -2C. The two formulas are indeed equivalent.
"""

