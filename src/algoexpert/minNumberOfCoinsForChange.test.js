// Add, edit, or remove tests in this file.
// Treat it as your playground!

const program = require('./program');
const chai = require('chai');

it('Test Case #1', function() {
  chai.expect(program.minNumberOfCoinsForChange(0, [1, 2, 3])).to.deep.equal(0);
});

it('Test Case #2', function() {
  chai.expect(program.minNumberOfCoinsForChange(3, [2, 1])).to.deep.equal(2);
});

it('Test Case #3', function() {
  chai
    .expect(program.minNumberOfCoinsForChange(4, [1, 5, 10]))
    .to.deep.equal(4);
});

it('Test Case #4', function() {
  chai
    .expect(program.minNumberOfCoinsForChange(7, [1, 5, 10]))
    .to.deep.equal(3);
});

it('Test Case #5', function() {
  chai
    .expect(program.minNumberOfCoinsForChange(10, [1, 5, 10]))
    .to.deep.equal(1);
});

it('Test Case #6', function() {
  chai
    .expect(program.minNumberOfCoinsForChange(11, [1, 5, 10]))
    .to.deep.equal(2);
});

it('Test Case #7', function() {
  chai
    .expect(program.minNumberOfCoinsForChange(24, [1, 5, 10]))
    .to.deep.equal(6);
});

it('Test Case #8', function() {
  chai
    .expect(program.minNumberOfCoinsForChange(25, [1, 5, 10]))
    .to.deep.equal(3);
});

it('Test Case #9', function() {
  chai.expect(program.minNumberOfCoinsForChange(7, [2, 4])).to.deep.equal(-1);
});

it('Test Case #10', function() {
  chai.expect(program.minNumberOfCoinsForChange(7, [3, 7])).to.deep.equal(1);
});

it('Test Case #11', function() {
  chai.expect(program.minNumberOfCoinsForChange(9, [3, 5])).to.deep.equal(3);
});

it('Test Case #12', function() {
  chai.expect(program.minNumberOfCoinsForChange(9, [3, 4, 5])).to.deep.equal(2);
});

it('Test Case #13', function() {
  chai
    .expect(program.minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1]))
    .to.deep.equal(3);
});

it('Test Case #14', function() {
  chai
    .expect(
      program.minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1, 60, 75]),
    )
    .to.deep.equal(2);
});

it('Test Case #15', function() {
  chai
    .expect(
      program.minNumberOfCoinsForChange(41, [25,10,5,1]),
    )
    .to.deep.equal(4);
});

it('Test Case #16', function() {
  chai
    .expect(
      program.minNumberOfCoinsForChange(41, [25,10,1]),
    )
    .to.deep.equal(5);
});

it('Test Case #17', function() {
  chai
    .expect(
      program.minNumberOfCoinsForChange(55, [25,10,1]),
    )
    .to.deep.equal(4);
});