export class Stack {
  #items = {};
  #count = 0;

  /**
   * Insert new elements to the top (end) of the stack
   */
  push(item) {
    this.#items[this.#count] = item;
    this.#count++;
  }

  /**
   * Remove the element on the top of the stack and returns it
   */
  pop() {
    if (this.isEmpty()) return undefined;
    
    this.#count--;
    const item = this.#items[this.#count];
    delete this.#items[this.#count]
    return item;
  }

  /**
   * Return the element on the top of the stack
   */
  peek() {
    return this.#items[this.#count - 1];
  }

  /**
   * Returns if stack has items
   */
  isEmpty() {
    return !this.#count;
  }

  /**
   * Remove all the elements from the stack
   */
  clear() {
    return this.#items = {};
  }

  /**
   * Returns the count of all elements in list
   */
  size() {
    return this.#count;
  }

  /**
   * To string
   */
  toString() {
    if (this.isEmpty()) return '';

    let objString = `${this.#items[0]}`
    for (let i = 1; i < this.#count; i++) {
      objString = `${objString},${this.#items[i]}`;
    }
    return objString;
  }
}