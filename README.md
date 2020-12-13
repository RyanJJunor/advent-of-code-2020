# advent-of-code-2020

<h1><b>Day 1.</b></h1>
Included two solution for both part one and part two.<br>
The two functions for task one take very similar times.<br>
For part two, the second solution out performs the first with the first taking ~0.2 seconds and the second taking ~0.03 seconds.

<h1><b>Day 2.</b></h1>
Not the most elegent solution, but a solution.<br>

<h1><b>Day 3.</b></h1>
Quite happy with my solution, I chose to try and write the solution to part one in a way that would be maybe useful for part two, before having seen part two and it worked well. As my solution for part one calculates how many trees would be hit in a certain map when given a certain slope, I was able to just pass in the list and relevant slope for each journey in part two in to my solution for part one and multiply all of the results together. <br>
<br>
<b>Edit.</b><br>After seeing other solutions I went back and added a second solution which I like better, where instead of actually extending the map to the right as                   many times as needed, I use modulo to reuse the given map by looping back to the beginning when there is an overflow. Quite disappointed that I didn't think of it actually.<br>

<h1><b>Day 4.</b></h1>
This felt like quite a decent jump in complexity.<br>
I'm quite happy with my solution, I learned a new technique, a way of finding if all elements from a list are present in another list:<br>
<br><i>if all(x in list for x in required_elements):</i><br><br>
I can see that coming in useful.<br>
This one was a good challenge.

<h1><b>Day 5.</b></h1>
Nice and quick part two.
I was quite happy with my solution where I was manually changing the upper and lower bounds of the region based the character encountered.<br>
Then I came across the binary solution and my mind was blown. It's so nice and elegant. I had to add in to my code.<br>

<h1><b>Day 6.</b></h1>
Nothing too special but still enjoyed it, savouring these more simple ones while I can.<br>


<h1><b>Day 7.</b></h1>
Had to really stop and think through what it was that I wanted to do. This one was a good challenge.<br>

<h1><b>Day 8.</b></h1>
A nice wee challenge, I was thinking that this could be one that gets built upon in future days so I made an attempt at writing classes in Python, my first time doing so, so I need to check if I did it correctly. There is definitely a lot of room for improvement in my code this week so I would like to come back to it and make it nicer.<br>

<h1><b>Day 9.</b></h1>
Had to take a day off, so did this one on the 10th, wasn't too difficult.<br>

<h1><b>Day 10.</b></h1>
Also started this one on the 10th, however it wasn't until around 1 am on the 12th that I managed to get a solution to part 2.<br>
I was determined to not look anything up, I wanted to figure it out by myself. My first attempt used recursion to navigate through the entire tree structure that I made, that would have just taken too long to run, my next solution kept a running list containing each adapter's 'joltage' rating where each rating would appear in the list, as many times as it would in the tree, so I guess a flattened tree? This solution caused a memory error.<br><br>
Finally I landed on my final solution which was essentially the same idea as the previous one, but rather than maintaining a huge list  where I was having to count how many times a specific adapters 'parent adapter' appeared in the list, I changed it to a dictionary, where the key was the 'joltage' rating of an adapter, and the value was how many times that adapter would appear in the tree. This made it much faster, with the whole process of finding the number of different combinations taking 0.0 seconds according to Python. To get the answer from this dictionary, I just returned the number of time that the largest key (joltage) would have occured.<br>
Definitely not the best solution, but it's the one I came up with.<br>

<h1><b>Day 11.</b></h1>
Struggled along with part 2 for quite a while making changes I didn't need to because I accidentally had a != instead of a ==.<br>

<h1><b>Day 12.</b></h1>
A nice simple one, all caught up now.<br>
