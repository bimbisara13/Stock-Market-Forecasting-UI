import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})

export class StocksService {
  constructor() {}

  stocks = [
    {
      id: 1,
      name: 'TCS',
      mape: 0.77,
      rmse: 0.42,
      mae: 0.5,
      mbe: 0.012,
    },
    {
      id: 2,
      name: 'Adobe Inc.',
      mape: 0.79,
      rmse: 0.46,
      mae: 0.51,
      mbe: 0.009,
    },
    {
      id: 3,
      name: 'Salesforce, Inc.',
      mape: 0.81,
      rmse: 0.39,
      mae: 0.508,
      mbe: 0.01,
    },
    {
      id: 4,
      name: 'The Boeing Company',
      mape: 0.66,
      rmse: 0.49,
      mae: 0.49,
      mbe: 0.006,
    },
    {
      id: 5,
      name: 'Tesla, Inc.',
      mape: 0.64,
      rmse: 0.51,
      mae: 0.502,
      mbe: 0.014,
    },
    {
      id: 6,
      name: 'NVIDIA Corporation',
      mape: 0.85,
      rmse: 0.42,
      mae: 0.48,
      mbe: 0.009,
    },
    {
      id: 7,
      name: 'Pfizer, Inc. Common Stock',
      mape: 0.77,
      rmse: 0.48,
      mae: 0.5,
      mbe: 0.016,
    },
    {
      id: 8,
      name: 'JP Morgan Chase & Co.',
      mape: 0.71,
      rmse: 0.41,
      mae: 0.51,
      mbe: 0.018,
    },
  ];
}
