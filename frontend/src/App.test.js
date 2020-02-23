import React from 'react';
import { render } from '@testing-library/react';
import App from './components/App';

test('renders semesterplaner link', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/Semesterplaner/i);
  expect(linkElement).toBeInTheDocument();
});
