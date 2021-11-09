/*----------------------------------------------------------------------------
 * Name:    CAN.h
 * Purpose: CAN interface for LPC17xx
 * Version: V1.00
 * Note(s):
 *----------------------------------------------------------------------------
 * This file is part of the uVision/ARM development tools.
 * This software may only be used under the terms of a valid, current,
 * end user licence from KEIL for a compatible version of KEIL software
 * development tools. Nothing else gives you the right to use this software.
 *
 * This software is supplied "AS IS" without warranties of any kind.
 *
 * Copyright (c) 2009 Keil - An ARM Company. All rights reserved.
 *----------------------------------------------------------------------------
 * History:
 *          V1.00 Initial Version
 *----------------------------------------------------------------------------*/

#ifndef _CAN_H_
#define _CAN_H_

#define STANDARD_FORMAT  0
#define EXTENDED_FORMAT  1

#define DATA_FRAME       0
#define REMOTE_FRAME     1

typedef struct  {
  unsigned int   id;                    /* 29 bit identifier */
  unsigned char  data[8];               /* Data field */
  unsigned char  len;                   /* Length of data field in bytes */
  unsigned char  format;                /* 0 - STANDARD, 1- EXTENDED IDENTIFIER */
  unsigned char  type;                  /* 0 - DATA FRAME, 1 - REMOTE FRAME */
} CAN_msg;

/* Functions defined in module CAN.c */
void CAN_setup         (int ctrl);
void CAN_start         (int ctrl);
void CAN_waitReady     (int ctrl);
void CAN_wrMsg         (int ctrl, CAN_msg *msg);
void CAN_rdMsg         (int ctrl, CAN_msg *msg);
void CAN_wrFilter      (int ctrl, int id, int filter_type);

extern CAN_msg       CAN_TxMsg[2];      /* CAN messge for sending */
extern CAN_msg       CAN_RxMsg[2];      /* CAN message for receiving */                                
extern unsigned int  CAN_TxRdy[2];      /* CAN HW ready to transmit a message */
extern unsigned int  CAN_RxRdy[2];      /* CAN HW received a message */

#endif // _CAN_H_


