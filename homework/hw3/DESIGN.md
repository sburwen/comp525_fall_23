### __str__(self) function
* Initialize empty string `ul_str`
* Initialze variable `curr_node` to head
* Begin loop while `curr_node` is not `None`
  * If the current node's `get_next` property is `None`, concatenate the current node's `get_data` property to `ul_str`
    * Else, concatenate the current node's `get_data` property _and_ a `,` to `ul_str`
  * Set the current node to its `get_next` property
  * Return `ul_str`
### append(self, item) function
* Initialize variable `new_node` as Node object with `item`
* Initialze varibale `curr_node` as head
* If `curr_node` is `None`: set `next` property of `new_node` to `None` and set head to `new_node`
  * Else, begin loop while `curr_node` is not `None`
  * If the `next` property of `curr_node` is `None`: set the `next` property of `new_node` to `None` and set the next 
  property of `curr_node` to `new_node`
  * Break out of the loop
* Set the current node to its `get_next` property