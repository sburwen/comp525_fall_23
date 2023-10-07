### count() function
* Take `num_list` and `num` as inputs. Goal is to count how many times num appears in list.
* Initialize local variable `counter` to `0`.
* Begin for loop which iterates using `i` for length of the list.
  * Inside for loop, increase counter by 1 if `i` is equal to `num`.
* After loop, return `counter`.

### extend() function
* Take `num_list` and `another_num_list` as inputs. Goal is to create a new list with the 2nd list added after the 1st.
* Initialize `new_list` as list equal to `num_list`.
* Begin for loop which iterates using `i` for items in `another_num_list`.
  * Inside for loop, append `i` to `new_list`.
* After loop, return `new_list`.

### remove() function
* Take `num_list` and `num` as inputs. Goal is to remove instances of `num` from `num_list`.
* Initialzie `new_list` as empty list.
* Begin for loop iterating using `i` for items in `num_list`.
  * Inside for loop, if `i` does not equal `num`, append it to `new_list`.
  * Else pass.
* After loop, return `new_list`.

### index() function
* Take `num_list` and `num` as inputs. Goal is to find index of `num`.
* Initialize local variable `counter` to `0`.
* Initialize local variable `flag` to `0`.
* Begin for loop which iterates using `i` for length of the list.
  * If `i` is equal to `num`, break and set flag to 1.
    * Else increase counter by `1`.
* After loop, if `flag` is equal to `0`, set `counter` equal to `None`
* Return `counter`.