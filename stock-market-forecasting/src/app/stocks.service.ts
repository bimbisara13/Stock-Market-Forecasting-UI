import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StocksService {

  constructor() { }

  stocks = [
    { id: 1, name: 'TCS' },
    { id: 2, name: 'Adobe Inc.' },
    { id: 3, name: 'Salesforce, Inc.' },
    { id: 4, name: 'The Boeing Company' },
    { id: 5, name: 'Tesla, Inc.' },
    { id: 6, name: 'NVIDIA Corporation' },
    { id: 7, name: 'Pfizer, Inc. Common Stock' },
    { id: 8, name: 'JP Morgan Chase & Co.' },
  ];
}
