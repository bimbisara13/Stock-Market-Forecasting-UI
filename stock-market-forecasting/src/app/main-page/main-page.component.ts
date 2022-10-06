import { Component, OnInit } from '@angular/core';
import { Stocks } from './main-page-interface';
@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})

export class MainPageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  stocks: Stocks[] = [
    {value: 'tcs', viewValue: 'TCS'},
    {value: 'adobe', viewValue: 'Adobe Inc.'},
    {value: 'salesforce', viewValue: 'Salesforce, Inc.'},
    {value: 'boeing', viewValue: 'The Boeing Company'},
    {value: 'tesla', viewValue: 'Tesla, Inc.'},
    {value: 'nvidia', viewValue: 'NVIDIA Corporation'},
    {value: 'pfizer', viewValue: 'Pfizer, Inc. Common Stock'},
    {value: 'jpmorgan', viewValue: 'JP Morgan Chase & Co.'},
  ];

}
