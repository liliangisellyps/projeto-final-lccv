import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AccordionModule } from 'ngx-bootstrap/accordion';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { MenuComponent } from './menu/menu.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RegisterComponent } from './modules/belogings/components/register/register.component';
import { HomeComponent } from './modules/belogings/components/home/home.component';
import { ListComponent } from './modules/belogings/components/list/list.component';
import { TabsModule } from 'ngx-bootstrap/tabs';
import { ModalModule } from 'ngx-bootstrap/modal';
import { BsDatepickerModule } from 'ngx-bootstrap/datepicker';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    MenuComponent,
    RegisterComponent,
    HomeComponent,
    ListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AccordionModule.forRoot(),
    BrowserAnimationsModule,
    TabsModule.forRoot(),
    ModalModule.forRoot(),
    NgbModule,
    BsDatepickerModule.forRoot() 
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
