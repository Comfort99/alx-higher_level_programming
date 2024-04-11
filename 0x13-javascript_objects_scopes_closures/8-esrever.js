#!/usr/bin/node
exports.esrever = function (list) {
  /* check if the list is empty */
  if (list.legth <= 1) {
    return list.slice(); /* return copy */
  }
  /* swap the elements of the list */
  let start = 0;
  let end = list.length - 1;

  while (start < end) {
    const temp = list[start];
    list[start] = list[end];
    list[end] = temp;

    /* triverse the through the list */
    start++;
    end--;
  }
  return list;
};
