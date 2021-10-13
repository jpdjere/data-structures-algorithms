# Section 4 - How to Solve Coding Problems

## What are companies looking for?

1. **Analytic Skills:** how well can you think through a problem and analyze things? When you are coding during an interview, do you explain your thought process and show how you go from not knowing the answer to solving the problem?
2. **Coding Skills:** do you code well? Is your code clean? Well-organized? Readable? 
3. **Techincal Skills:**  o Do you have the technical knowledge needed? Do you know the fundamentals? Did you just memorize things or do you understand the pros and cons of different solutions?
4. **Communication Skills:** Can you communicate well with others, and with a team? You won't be working by yourself, but with other engineers, bosses, managers. Does your personality match the company's personality?

Most peope get obsessed with the idea of learning every single algorithm and data structure before an interview. While these are important, you don't actually need to know how to write a binary search tree or write a sorting algorithm from scratch. Most of the time you learn it on the go on the job when you need it, or search the Web for ansers. Nobody has every single thing memorized.

What companies are looking for are people who know to to look for answers. They want to know that you know of the existence of the different data structures and algorithms, and that you know how and when to choose one over the other.

## What we need for Coding Interviews

During this course we will go through the following topics:

### Data Structures

1. Arrays
2. Stacks
3. Queues
4. Linked Lists
5. Trees
6. Tries
7. Graphs
8. Hash Tables

### Algorithms

1. Sorting
2. Dynamic Processing
3. BFS + DFS (Searching)
4. Recursion

While there are many more data structures and algorithms, we will only focus on this ones, which are the most used.

## Excercise: Google Interview

### Step by Step through a problem

1. When the interviewer explains the question, write the main points down. Show how organized you are. Make sure you have all the details. For example, is the input array sorted?
2. Make sure you know what the **inputs** are and what the **output** should be.
3. What is most important to optimize in the problem? Time complexity, space complexity?
4. Ask questions to clarify the problem given but don't be annoying by asking too many.
5. Start with naive/brute force approach. The easiest and most straight forward thing that comes to mind. **Don't** write down this solution, just explain it out loud.
6. Explain to the interviewer why this approach is not the best: time complexity too high, i.e. O(N^2), space complexity too high, or the code is not readable.
7. Before you start coding, walk through your chosen solution, and write down the steps you are going to follow.
8. Since a lot of interviews ask questions that you won't be able to answer fully on time, think: what can I show in order to demonstrate that I can solve this? Break things up in functions (if you don't remember a method, make it up). Alway write something and start with the easy part.
9. Think about error checks and how the code can be broken. Don't make assumptions about the input. Check for false inputs and edge cases. Explain to the interviewer how would you test your code.
10. Use readable code and expressive variables: don't just name your variables i and j.
11. Test your code: use a couple of examples that the interviewer might give you to do a test run on your code, or even invent your own input cases to test it.
12. Finally, talk to the interviewer about where you would improve the code with more time. Are there other different approaches? Is it readable? How can performance be improved. Maybe even ask the interviewer what was the most interesting solution they have seen to the problem.
13. The interviewer might ask you extension questions, such as how would you handle the problem if the whole input is too large to fit into memory, or if the input arrives as a stream. This is a common follow-up question at Google, where they care a lot about scale. The answer is usually to use a divide-and-conquer approach: perform distributed processing of the data and only read certain chunks of the input from disk into memory, write the output back to disk and combine them later.

### Heuristics to ace the question

- The time complexity should be less than O(N^2). Avoid nested loops. Two separate loops are better than two nested loops.
- Pay attention to space complexity: recursion can cause stack overflow, and copying large arrays may exceed memory of machine.
- Try sorting your input (or ask if you can assume it's sorted). If it is sorted, you can use a binary tree to achieve O(log N), use divide and conquer or a binary search.
- Hash Maps/Table are usually a wat of improving time complexity (might come with a memory cost).
- Analyze the Time vs Space tradeoff: Sometimes storing extra state in memory can help with time. More spaced is used to get a time optimization.

### Google Interview - How to: Work at Google — Example Coding/Engineering Interview

**INTERVIEWER:** I'm giving you a colelction of numbers, and you need to find a matching pair of numbers which is equal to a sum that I will also give you. For example:
```ts
[1,2,3,9]  Sum = 8
[1,2,4,4]  Sum = 8
```

**CANDIDATE:** So in the first example, you are looking for a pair of numbers that add up to 8, so in this example, there are none. And in the second one, we have the pair of 4s.

**INTERVIEWER:** That's correct. 

**CANDIDATE:** So how are these numbers given? Can I assume they are in memory?

**INTERVIEWER:** Yes, they are in memory and in an array, and you can also assume that they are ordered.

**CANDIDATE:** OK. And how about repeating elements? Can I assume they will be, for instance, in the second array, if I didn't have the last 4, can I use the remaining 4 combined with itself to get the 8?

**INTERVIEWER:** You can't repeat or reuse the number at the same index twice, but the same number may appear twice.

**CANDIDATE:** What about the numbers? Can I assume they will be all integers, or also floating points?

**INTERVIEWER:** You can assume that they will all be integers, but negatives can happen. 

**CANDIDATE:** OK. Cool. The simplest solution of course would be to compare every single possible pair, so I could just have two for-loops, one scanning the whole array, and the second one, starting from i+1, if the first has an index of 1, so I don't repeat the same value. And for every iteration I would test if the sum is equal to the target sum. But that wouldn't be an efficient way to solve it [It would have a time complexity of O(N^2)].

**INTERVIEWER:** That would work, but it'd be time consuming. Is there any other way it could work? 

**CANDIDATE:** Yes, that would have a quadratic time complexity. So, let's find a better way. Since it's sorted... When I'm standing on a number, what I'm looking for is if in the rest of the array there's another number which I can sum it up with to reach the objective sum. So in the first example, for example, when I check the 1, I need to find out if in the rest of the array there's a 7 to sum up to 8. If that the case, and because it is sorted, I can do binary search: I can loop through the array, and for example, when standing on the first element, I would binary search through the rest of the array (i.e. [2,3,9]) to try to find a 7. And as I don't find it, I'll continue on the loop and then standing on the second element (the 2), I would binary search on the rest of the array (i.e. [3,9]), and so on, until I found it, or I reached the last element, which means there are no pairs. That's better than quadractic: binary search is a log algorithm [O(log N)] in a sorted list, and since I'm doing a search for every element in the array the time complexity would be O(N log N).

**INTERVIEWER:** Also an answer... but still a little bit slow. So what if instead of doing a binary search which is unidrectional, what is you started with a pair of numbers to begin with and then worked your way from there?

**CANDIDATE:** Let's see, let me think about this. So, the largest possible sum would be the two last numbers in the array, and the smallest possible sum would be the sum of the first two. So the range of the possible values is between the first element and the last element: there's nothing smaller than the first value and nothing bigger than the last value. So from there we have somewhere to move from.
```ts
[1,2,3,9]  Sum = 8
 ‾     ‾
```
So if the sum of the first number and the last number, which in this case is 10, is too large, I need to find a smaller sum, so I can move the selected largest number to a smaller one:
```ts
[1,2,3,9]  Sum = 8
 ‾   ‾  
```
And if that is too small now (it sums 4), then I need to move the smallest one to one higher:
```ts
[1,2,3,9]  Sum = 8
   ‾ ‾  
```
So yes, I think I can do it this way in a linear solution: at each iteration I either move the high one lower if the sum of my pair is too large, or move the lower one higher if my pair is too small. And I end either when I find a pair that sums to the objective sum, or whenever they cross, i.e. the indeces of the pair are the same. At every iteration I'm moving exactly one of them, and that means it a linear way of solving this.

**INTERVIEWER:** And how does that make it faster than a binary search?

**CANDIDATE:** In the binary search case I was doing log for finding, but I had to repeat that for every element, so I was ending up with time complexity of O(N log N). In this case, I just need to scan the array one time, so it's a linear solution, which is faster.

**INTERVIEWER:** Before we get to coding it, can you explain it with the other (working) example? 

**CANDIDATE:** So in this case, I would start with the indeces at the extremes:
```ts
[1,2,4,4]  Sum = 8
 ‾     ‾  
```
The sum is 5, which is smaller than 8, so I'd move the lower index up.
```ts
[1,2,4,4]  Sum = 8
   ‾   ‾  
```
The sum is 6, which is smaller than 8, so I'd move the lower index up again.
```ts
[1,2,4,4]  Sum = 8
     ‾ ‾  
```
And here the sum is 8, so we've reached our targeted sum. That's true and I would return.

**INTERVIEWER:** OK, cool, so let's code it.

**CANDIDATE:** All right. First of all, I realized that I don't know what I want my function to return. Do I return the pair of numbers, the indeces of the pair, or whether I just found it or not?

**INTERVIEWER:** For the purposes of this example, we'll go for whether if you found it or not, but, if you needed to return the pair, how would that become a problem if there was no pair?

**CANDIDATE:** Well, building the pair would be easy, just return it. But if I didn't find it, I would need to return some sort of boolean. I guess I could make a data structure that has a boolean, that denotes whether the pair has been found. Something like:
```ts
type res = {
  found: boolean;
  pair: number[];
} 
```
And we would return this whole data structure. It's not very elegant, but it's workable.

**INTERVIEWER:** OK. Let's code it. For now it's OK to just return a boolean.

**CANDIDATE:** Right. Ok, so let's call our function `hasPairWithSum`, which will return a `boolean`, and I'll assume the input will be an array of integers, and then I have another input which is a integer which is my `sum`.

```ts
const hasPairWithSum = (data: number[], sum: number): boolean => {

}
```
So I'll start first by initiating my lower and higher indices:
```ts
const hasPairWithSum = (data: number[], sum: number): boolean => {
  let low = 0;
  let high = data.length - 1;
}
```
And then, what I'm going to do is: while my `low` is strictly lower than my `high`... as soon as they are touching I know I can't guarantee that they are different... so that's where I should stop:
```ts
const hasPairWithSum = (data: number[], sum: number): boolean => {
  let low = 0;
  let high = data.length - 1;
  while(low < high) {

  }
}
```
This condition within the `while` will also solve the issue of what happens when `data` is empty. Because if `data` is empty, then `high` would be `-1` and the condition would be violated in the first check, before we try to access any of the values.
So, now I can sum my `low` and `high` and compare if they equal my `sum`:
```ts
const hasPairWithSum = (data: number[], sum: number): boolean => {
  let low = 0;
  let high = data.length - 1;
  while(low < high) {
    if(data[low] + data[high]) {
      // Here's where I would construct the data structure
      // we mentioned if we wanted to return that instead.
      return true
    }
  }
}
```
Now, if the sum is larger than `sum` or it is lower than `sum`, then I had to adjust the indices. So I'd better do the sum once and store it in a variable instead.
```ts
const hasPairWithSum = (data: number[], sum: number): boolean => {
  let low = 0;
  let high = data.length - 1;
  while(low < high) {
    const probableSum = data[low] + data[high];
    if(probableSum === sum) {
      return true
    } else if(probableSum < sum) {
      low = low + 1
    } else {
      high = high - 1;
    }
  }
  return false;
}
```

10.53
**INTERVIEWER:** OK. I'm gonna stop you right there. Excellent solution. But now: I can no longer guarantee that the numbers in this collection are sorted. You have to find another way of comparing them against each other now.

**CANDIDATE:** Well, if the first thing I do is sort, then I can solve the problem in the same way. That would be still an O(N log N) solution, which is the same as the solution with the binary search.

**INTERVIEWER:** Yes, but that's still too slow for Google! 

**CANDIDATE:** OK, let's see. If I go back to this idea of, when I look at a number, what I'm trying to figure out is if I've seen its complement to reach the sum. So for example, in the first example, when standing on the first element 
```ts
[1,2,3,9]  Sum = 8
 ‾     
```
I need to find out if a 7 is in the rest of the array. If I cannot sort, and searching the rest of the array per element would be quadratic... maybe I can do it the other way around: I can build something up (some data structure) and for each iteration I can simply ask: have I seen the complement before? So for example, if I'm here:
```ts
[1,2,3,9]  Sum = 8
     ‾
```
what I need to find if I have seen the complement of 3 before. Have I seen a 5 before?
Or, I guess it's the same, I could be storing the complements, and in each iteration I could ask: have I seen the number I'm seeing now as a complement of the numbers I've seen before? So in the first example: I start iterating and on the first one I insert a 7 as complement to one, I insert a 6 as complement of 2, etc.
```ts
 7 6
[1,2,3,9]  Sum = 8
     ‾
```
And for each iteration I can ask, have I seen the complement before?... just by checking if my current number is already stored in my data structure (because I have stored it as the complement before).
I can use a data structre that is very good for lookups, like a hashtable, which has a constant time loookup.

**INTERVIEWER:** Hashtable though? With key value pairs? Do you need a key in this case?

**CANDIDATE:** I actually just need the value, each element, so I don't need to store any payload, so... a hashset would be the way to go. I can hashset all of the complements and then I look up for them... I need to be careful though: how am I going to deal with the case of repeated elements? Because I don't want to be able to stand on a 4 and say: OK, I have a 4 (which I just added) on my set, so I'm done. And that would be a wrong solution. But if for every element I just look for elements that I added to my set **before** the number I'm standing on, it should work. So I need to do the check for the complement in my set, **before** inserting the complement of my current number to the set. So, now, once I', standing on my repeated number, I do the check for all numbers before, and that should work:
```ts
[1,2,4,4]  Sum = 8
       ‾
```

**INTERVIEWER:** All right. So let's code it.

**CANDIDATE:** Ok, so:
```ts
const hasPairWithSum = (data: number[], sum: number): boolean => {
  const complements = new Set<number>();
  for(const num of data) {
    if(complements.has(num)) {
      return true;
    }
    complements.add(sum-num)
  }
  return false;
}
```
I need I need to run through an example to test if this actually works. So first of all, I have nothing in my set, and I check for my first value which is a one. Of course, I don't find anything in my set, so I add my complement to my set which is 7 (8 minus 1).
```ts
[1,2,3,9]  Sum = 8
 ‾     
complements = {7}

[1,2,4,4]  Sum = 8
 ‾     
complements = {7}
```

Then I go for thw two, I look whether there's a 2 on the set. There isn't, so I add it to the set:
```ts
[1,2,3,9]  Sum = 8
   ‾   
complements = {7,6}

[1,2,4,4]  Sum = 8
   ‾   
complements = {7,6}
```

And here is where the examples start to diverge. First I check on the top: have I seen the complement of a 3? No. Then I add it to the set. And the same with the four.
```ts
[1,2,3,9]  Sum = 8
     ‾   
complements = {7,6,5}

[1,2,4,4]  Sum = 8
     ‾   
complements = {7,6,4}
```
And then in the last one, for the top example, I'd check if I've seen the complement of 9 (which should be -1), and as I haven't I would add it.
```ts
[1,2,3,9]  Sum = 8
       ‾   
complements = {7,6,5,-1}
```
And then the for-loop ends and I'd return `false`.

In the bottom example, when standing on the last element, I would first check if I already saw the complement of 4, which is also 4. As I have (it is present in my Set), I would return `true`.
```ts
[1,2,4,4]  Sum = 8
       ‾   
complements = {7,6,4}
```

So, one more thing: what happens with an empty `data` array? Well, the empty set won't be looped over in the for-loop precisely because it is empty. So it will return `false` always.

So this is the right solution. And it runs in linear time, with tome complexity O(N) because: for each iteration we are doing constant time operations (lookup in a Set and adding in a Set), and I do it for all the values in the input of size N.

And memory (space) complexity is linear as well because in the worst case scenario I have added all of the elements in the input to the Set.

**INTERVIEWER:** Would you do anything different if the input had a size of ten million integers?

**CANDIDATE:** Would it still fit in memory?


**INTERVIEWER:** Probably not at this point.

**CANDIDATE:** OK, then if it doesn't fit in memory... Is the range of the values limited in some way?

**INTERVIEWER:** You can assume they might be.

**CANDIDATE:** Then if my set fits in memory, but my whole input doesn't, then I can process the input in chunks, and accumulate the complements in a set. If we can do it in parallel, it is kind of the same thing: we would have now multiple computers, each one processing a chunk of the input, and each producing a set of complements for each chunk which it has seen, and we would just merge the sets, and evaluate all the inputs against that.

The merging would be a little bit tricky, because we want to make sure that we don't look up for the number I just added to the set (like a 4 finding itself as complement in the set, when it was just added). But as long as each individual computer is doing the check and the addition in the right order (as we are above), when we merge them we can guarantee that they are correctly added to the set. So if we had a 4 in one computer and another 4 in another computer, we'd have to be carefuel when merging that we reconcile them, but that would be the only consideration.

**INTERVIEWER:** Right, great job.

**INTERVIEWER:** So, just to recap that interview: a couple of things one should be aware of when interviewing:

**1. Ask for a clarification of the problem:** if you don't understand the question, feel free to ask for clarification or ask to have it repeated. You can write it down, whatever you need to do to get a full understanding of what's being asked. Some of his clarifications above where if the input allowed for negative numbers or floating point numbers, and that has an effect on how the problem is solved, so its great to ask.

**2. Think out loud constantly:** Even before starting to write code, and while you are going through the solution, think out loud. This gives the interviewer the opportunity to see your thought process and possibily correct you and point you to the question they were asking, and even feed off of that and ask you more questions that might help you demonstrate your knowledge even further.

**3. Think through everything before starting to write:** Think how we will do everything before starting to code. In the example, the candidate even goes through two different iterations before even starting to code. The first thing that came up out of the top of his mind wasn't the best solution, and it's not gonna be for anybody, but it's good to mention them and why it's not. Think them through out loud, and you might get challenged by the interviewer to think better, faster, quicker or more efficiently, think through that solution, and when you are both at the point where you can code it, then go ahead.

**4. Test it:** Test your solution in real time. Use the examples given by the interviwer or even make up one up if you don't have it. And test it out loud for your interviwer as well.

**5. Think about edge cases:** This are really important. In this example, the candidate thought of what happened if he had an empty collection of numbers, and he also tested what would happen with this solution for that edge case.
