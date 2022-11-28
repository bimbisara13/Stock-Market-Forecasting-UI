import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { FinancialDataService } from '../data.service';
import { ActivatedRoute } from '@angular/router';
import { StocksService } from '../stocks.service';
import { HttpClient } from '@angular/common/http';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  providers: [FinancialDataService],
  selector: 'app-analysis',
  templateUrl: './analysis.component.html',
  styleUrls: ['./analysis.component.css'],
})
export class AnalysisComponent implements OnInit {
  public data: any;
  stock: any;
  stockId: any;
  resData: any;
  ticker: any = this.activatedRoute.snapshot.paramMap.get('id');
  headers: any = ['Access-Control-Allow-Origin', '*'];
  public error: number = 0;

  constructor(
    private activatedRoute: ActivatedRoute,
    private service: StocksService,
    private http: HttpClient,
    private dataService: FinancialDataService
  ) {
    if (this.ticker == 'AAPL') {
      this.data = [this.dataService.getAapl()];
    } else if (this.ticker == 'AMZN') {
      this.data = [this.dataService.getAmzn()];
    } else if (this.ticker == 'CVS.F') {
      this.data = [this.dataService.getCvsf()];
    } else if (this.ticker == 'GE') {
      this.data = [this.dataService.getGe()];
    } else if (this.ticker == 'GOOGL') {
      this.data = [this.dataService.getGoogl()];
    } else if (this.ticker == 'IBM') {
      this.data = [this.dataService.getIBM()];
    } else if (this.ticker == 'MSFT') {
      this.data = [this.dataService.getMsft()];
    } else if (this.ticker == 'WMT') {
      this.data = [this.dataService.getWmt()];
    }
    this.error = this.data[0][2];
  }

  ngOnInit() {
    this.stockId = this.activatedRoute.snapshot.paramMap.get('id');
    this.stock = this.service.stocks.find((x) => x.id == this.stockId);
  }

  body: any = { stock_name: this.ticker };
  // sendRequest() {
  //   this.http
  //     .post<any>('http://127.0.0.1:8000/', this.body, this.headers)
  //     .subscribe((data) => {
  //       this.resData = data;
  //     });
  // }
}
