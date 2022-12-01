import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { StocksService } from '../stocks.service';
import { DataService } from '../data.service';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  providers: [],
  selector: 'app-analysis',
  templateUrl: './analysis.component.html',
  styleUrls: ['./analysis.component.css'],
})

export class AnalysisComponent implements OnInit {
  public data: any;
  stock: any;
  stockId: any;

  dateList: any = undefined || [];
  year: any;
  month: any;
  day: any;

  actualList: any = undefined || [];
  predictedList: any = undefined || [];

  result: any;

  requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      stock_name: this.activatedRoute.snapshot.paramMap.get('id'),
    }),
  };

  constructor(
    private activatedRoute: ActivatedRoute,
    private service: StocksService,
    private dataService: DataService
  ) {}

  async ngOnInit() {
    this.stockId = this.activatedRoute.snapshot.paramMap.get('id');
    this.stock = this.service.stocks.find((x) => x.id == this.stockId);
    this.data = await this.dataService.sendRequest(this.requestOptions);

    this.getProperData(
      this.data.df_plot.Actual,
      this.data.df_plot.Best_Model,
      this.data.df_plot.Date
    );
  }

  getProperData(actual: any, best: any, date: any) {
    console.log(date);
    for (const element of date) {
      this.dateList.push({
        year: element.slice(0, 4),
        monthIndex: element.slice(5, 7) - 1,
        day: element.slice(8, 10),
      });
    }

    for (let i = 0; i < date.length; i++) {
      this.actualList.push({
        time: new Date(
          this.dateList[i].year,
          this.dateList[i].monthIndex,
          this.dateList[i].day
        ),
        actual: actual[i],
      });
    }

    for (let i = 0; i < date.length; i++) {
      this.predictedList.push({
        time: new Date(
          this.dateList[i].year,
          this.dateList[i].monthIndex,
          this.dateList[i].day
        ),
        predicted: best[i],
      });
    }

    return [this.actualList, this.predictedList];
  }

  getData() {
    this.actualList.title = 'Actual';
    this.predictedList.title = 'Predicted';

    return [this.actualList, this.predictedList];
  }
}
