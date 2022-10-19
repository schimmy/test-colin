import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { IssueBoxComponent } from './issue-box/issue-box.component';
import { InspectionTableComponent } from './inspection-table/inspection-table.component';

@NgModule({
  declarations: [
    AppComponent,
    IssueBoxComponent,
    InspectionTableComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
