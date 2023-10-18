unction addDistinctElement(element) {
      if (!distinctElements.includes(element)) {
        distinctElements.push(element);
        sum += element;
      }
    }