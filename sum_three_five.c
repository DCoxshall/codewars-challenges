int findSum (int n) {
  long total = 0;
  for (int i = 0; i <= n; i++) {
    if (i % 5 == 0 || i % 3 == 0) {
      total += i;
    }
  }
  return total;
}
