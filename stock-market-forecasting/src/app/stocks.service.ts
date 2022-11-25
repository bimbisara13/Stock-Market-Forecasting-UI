import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class StocksService {
  constructor() {}

  stocks = [
    { id: 'AAPL', name: 'Apple, Inc.' },
    { id: 'ABC', name: 'AmerisourceBergen Corporation' },
    { id: 'ADM', name: 'Archer-Daniels-Midland, Co' },
    { id: 'AMZN', name: 'Amazon, Inc.' },
    { id: 'BAC', name: 'Bank of America Corporation' },
    { id: 'BRK-A', name: 'Berkshire Hathaway, Inc.' },
    { id: 'C', name: 'Citigroup, Inc.' },
    { id: 'CAH', name: 'Cardinal Health, Inc.' },
    { id: 'CI', name: 'Cigna Corporation' },
    { id: 'CMCSA', name: 'Comcast Corporation' },
    { id: 'CNC', name: 'Centene Corporation' },
    { id: 'COST', name: 'Costco Wholesale Corporation' },
    { id: 'CVS.F', name: 'CVS Health Corporation' },
    { id: 'CVX', name: 'Chevron Corporation' },
    { id: 'DELL', name: 'Dell Technologies, Inc.' },
    { id: 'ELV', name: 'Elevance Health, Inc.' },
    { id: 'F', name: 'Ford Motor Company' },
    { id: 'FDX', name: 'FedEx Corporation' },
    { id: 'FNMA', name: 'Federal National Mortgage Association' },
    { id: 'GE', name: 'General Electric Company' },
    { id: 'GM', name: 'General Motors Company' },
    { id: 'GOOGL', name: 'Alphabet Inc.' },
    { id: 'HD', name: 'The Home Depot, Inc.' },
    { id: 'HUM', name: 'Humana Inc.' },
    { id: 'IBM', name: 'International Business Machines Corporation' },
    { id: 'INTC', name: 'Intel Corporation.' },
    { id: 'JNJ', name: 'Johnson & Johnson' },
    { id: 'JPM', name: 'JPMorgan Chase & Co.' },
    { id: 'KR', name: 'The Kroger Co.' },
    { id: 'LOW', name: "Lowe's Companies, Inc." },
    { id: 'MCK', name: 'McKesson Corporation' },
    { id: 'MET', name: 'MetLife, Inc.' },
    { id: 'META', name: 'Meta Platforms, Inc.' },
    { id: 'MPC', name: 'Marathon Petroleum Corporation' },
    { id: 'MSFT', name: 'Microsoft Corporation' },
    { id: 'PEP', name: 'PepsiCo, Inc.' },
    { id: 'PFE', name: 'Pfizer, Inc.' },
    { id: 'PG', name: 'The Procter & Gamble Company' },
    { id: 'PSX', name: 'Phillips 66' },
    { id: 'STFGX', name: 'State Farm Growth FundApple, Inc.' },
    { id: 'T', name: 'AT&T, Inc.' },
    { id: 'TGT', name: 'Target Corporation' },
    { id: 'UNH', name: 'UnitedHealth Group Incorporated' },
    { id: 'UPS', name: 'United Parcel Service, Inc.' },
    { id: 'VLO', name: 'Valero Energy Corporation' },
    { id: 'VZ', name: 'Verizon Communications, Inc.' },
    { id: 'WBA', name: 'Walgreens Boots Alliance, Inc.' },
    { id: 'WFC', name: 'Wells Fargo & Company' },
    { id: 'WMT', name: 'Walmart, Inc.' },
    { id: 'XOM', name: 'Exxon Mobil Corporation' },
  ];
}
