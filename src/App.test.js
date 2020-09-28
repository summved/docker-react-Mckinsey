import React from 'react';
import { render } from '@testing-library/react';
import App from './App';
var AWS_ACCESS_KEY = "askdfhlksfdjadslkfjsfklj1232l3klsdkfjdsf";
var AWS_SECRET_ACCESS_KEY = "slkdajflsadf";
test('renders learn react link', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

it('renders learn react link', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
