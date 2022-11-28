import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { StocksService } from '../stocks.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-analysis',
  templateUrl: './analysis.component.html',
  styleUrls: ['./analysis.component.css'],
})
export class AnalysisComponent implements OnInit {
  stock: any;
  stockId: any;
  resData: any;
  headers: any = ['Access-Control-Allow-Origin', '*'];

  constructor(
    private activatedRoute: ActivatedRoute,
    private service: StocksService,
    private http: HttpClient
  ) {}

  ngOnInit() {
    this.stockId = this.activatedRoute.snapshot.paramMap.get('id');
    this.stock = this.service.stocks.find((x) => x.id == this.stockId);
  }

  body: any = { stock_name: this.activatedRoute.snapshot.paramMap.get('id') };

  sendRequest() {
    this.http
      .post<any>('http://127.0.0.1:8000/', this.body, this.headers)
      .subscribe((data) => {
        this.resData = data;
      });
  }
}
