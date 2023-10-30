### hide() function
* Initialize new dictionary `found_chars` as empty.
* Initialize variable `count` to 0.
* Initialize variable `new_sentence` to empty string.
* Begin loop for `char` in `sentence`.
  * If the character is found in values of `found_chars`, concatenate `*` to `new_sentence`.
  * Otherwise, concatenate `char` to `new_sentence` and add key-value pair of `count` and `char` 
  to `found_chars`.
  * Increment `count` by 1.
* Return `new_sentence`.

### reduce_adjacent() function
* Initialize list `new_num_list` as empty.
* Initialize variable `last` as empty string.
* Begin loop for `num` in `num_list`
  * If `num` is equal to `last`, pass.
  * Otherwise, append `num` to `new_num_list` and set `last` equal to `num`
* Return `new_num_list`.

### reverse() function
* Initialize `reverse_word` as empty string.
* Begin loop for `char` in `word`.
  * Set `reverse_word` equal to `char` concatenated in front of `reverse_word`.
* Return `reverse_word`.