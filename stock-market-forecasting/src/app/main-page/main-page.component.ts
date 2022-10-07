import { Component, OnInit } from '@angular/core';
import { Stocks } from './main-page-interface';
import { StocksService } from '../stocks.service';
@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css'],
})
export class MainPageComponent implements OnInit {
  selected: any = '';

  constructor(private service: StocksService) {
  }

  ngOnInit(): void {
  }

  stocks: Stocks[] = this.service.stocks;
}
