import 'package:dart/dart.dart';
import 'package:test/test.dart';

void main() {
  test('Exemplos dados', () {
    expect(somaMultiplos(10), 23);
    expect(somaMultiplos(11), 33);
  });

  test('Exemplos propostos', () {
    expect(somaMultiplos(20), 78);
    expect(somaMultiplos(25), 143);
  });
}
