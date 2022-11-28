import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class StocksService {
  constructor() {}

  stocks = [
    { id: 'AAPL', name: 'Apple, Inc.' },
    { id: 'AMZN', name: 'Amazon, Inc.' },
    { id: 'CVS.F', name: 'CVS Health Corporation' },
    { id: 'GE', name: 'General Electric Company' },
    { id: 'GOOGL', name: 'Alphabet Inc.' },
    { id: 'IBM', name: 'International Business Machines Corporation' },
    { id: 'MSFT', name: 'Microsoft Corporation' },
    { id: 'WMT', name: 'Walmart, Inc.' },
  ];
}
