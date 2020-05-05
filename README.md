# Daily Challenge #237 - Delete Extra Occurrences

[Dev.to challenge page](https://dev.to/thepracticaldev/daily-challenge-237-delete-extra-occurrences-3009)

## Description

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these gallery sessions, since the setting usually repeats. He isn't fond of seeing the Eiffel tower 40 times in a row. He tells them that he will only sit during the session if they only show the same setting at most N times. Luckily, Alice and Bob are able to encode each setting as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if `N = 2`, and the input is `[1,2,3,1,2,1,2,3]`, you take `[1,2,3,1,2]`, drop the next `[1,2]` since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to `[1,2,3,1,2,3]`.

### Examples

```
delete_nth([1,1,1,1],2) # return [1,1]

delete_nth([20,37,20,21],1) # return [20,37,21]
```

### Tests

```
delete_nth([1,1,3,3,7,2,2,2,2]), N= 3

delete_nth([20,37,20,21]), N = 1
```
