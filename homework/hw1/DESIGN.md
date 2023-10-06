### count() function
* Take `num_list` and `num` as inputs. Goal is to count how many times num appears in list.
* Initialize local variable `counter` to `0`.
* Begin for loop which iterates using `i` for length of the list.
  * Inside for loop, increase counter by 1 if `i` is equal to `num`.
* After loop, return `counter`.

### extend() function
* Take `num_list` and `another_num_list` as inputs. Goal is to create a new list with the 2nd list added after the 1st.
* Begin for loop which iterates using `i` for items in `another_num_list`.
  * Inside for loop, append `i` to `num_list`
* After loop, return `num_list`