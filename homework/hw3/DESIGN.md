### __str__() function
* Initialize empty string `ul_str`
* Initialze variable `curr_node` to head
* Begin loop while `curr_node` is not `None`
  * If the current node's `get_next` property is `None`, concatente the current node's `get_data` property to `ul_str`
    * Else, concatenate the current node's `get_data` property _and_ a `,` to `ul_str`
  * Set the current node to its `get_next` property
  * Return `ul_str`