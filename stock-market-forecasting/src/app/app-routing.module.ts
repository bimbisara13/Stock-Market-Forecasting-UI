import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { MainPageComponent } from './main-page/main-page.component';
import { AnalysisComponent } from './analysis/analysis.component';

const routes: Routes = [
  { path: '', component: HomePageComponent },
  { path: 'main', component: MainPageComponent },
  { path: 'analysis/:id', component: AnalysisComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
export const routingComponents = [HomePageComponent, MainPageComponent, AnalysisComponent];
