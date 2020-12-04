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
<b>Edit.</b><br>After seeing other solutions I went back and added a second solution which I like better, where instead of actually extending the map to the right as                   many times as needed, I use modulo to reuse the given map by looping back to the beginning when there is an overflow<br>

<h1><b>Day 4.</b></h1>
This felt like quite a decent jump in complexity<br>
I'm quite happy with my solution, I learned a new technique, a way of finding if all elements from a list are present in another list:
<br>if all(x in list for x in required_elements)<br>
I can see that coming in useful.<br>
This one was a good challenge.
