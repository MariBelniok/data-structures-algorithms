export class Stack {
  #items = []

  /**
   * Insert new elements to the top (end) of the stack
   */
  push(item) {
    this.#items.push(item);
  }

  /**
   * Remove the element on the top of the stack and returns it
   */
  pop() {
    return this.#items.pop();
  }

  /**
   * Return the element on the top of the stack
   */
  peek() {
    return this.#items[this.#items.length - 1];
  }

  /**
   * Returns if stack has items
   */
  isEmpty() {
    return !this.#items.length;
  }

  /**
   * Remove all the elements from the stack
   */
  clear() {
    return this.#items = [];
  }

  /**
   * Returns the count of all elements in list
   */
  size() {
    return this.#items.length;
  }
}