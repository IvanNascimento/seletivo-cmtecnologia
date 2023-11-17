int somaMultiplos(int numero) {
  int total = 0;

  for (int i = 0; i < numero; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      total += i;
    }
  }

  return total;
}
