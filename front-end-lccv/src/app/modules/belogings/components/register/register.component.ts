import { Component, OnInit, TemplateRef } from '@angular/core';
import {Location} from '@angular/common';
import { BsModalService, BsModalRef } from 'ngx-bootstrap/modal';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})

export class RegisterComponent implements OnInit {

  constructor(private modalService: BsModalService, private _location: Location) {}
  ngOnInit(): void {
  }

  modalRef?: BsModalRef;
 
  openModal(template: TemplateRef<any>) {
    this.modalRef = this.modalService.show(template);
  }

  backClicked() {
    this._location.back();
  }
  
}
