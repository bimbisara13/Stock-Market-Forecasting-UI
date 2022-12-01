import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})

export class DataService {
  constructor() {}

  resData: any;
  response: any;
  error: any;

  async sendRequest(requestOptions: {
    method: string;
    headers: { 'Content-Type': string };
    body: string;
  }) {
    this.response = await fetch('http://127.0.0.1:8000/', requestOptions);
    this.resData = await this.response.json();

    return this.resData;
  }

}
