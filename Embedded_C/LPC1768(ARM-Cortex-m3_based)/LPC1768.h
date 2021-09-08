/*
** Contains all the necessary definations of commonly used registers
** Can be edited to include more peripheral registers in the same fashion refering to Datasheet
*/

#ifndef LPC1768_INCLUDES_H
#define LPC1768_INCLUDES_H

//PINSELs
#define PINSEL0        	(*((volatile unsigned long *) 0x4002C000))
#define PINSEL1        	(*((volatile unsigned long *) 0x4002C004))
#define PINSEL2        	(*((volatile unsigned long *) 0x4002C008))
#define PINSEL3        	(*((volatile unsigned long *) 0x4002C00C))
#define PINSEL4        	(*((volatile unsigned long *) 0x4002C010))
#define PINSEL5        	(*((volatile unsigned long *) 0x4002C014))
#define PINSEL6        	(*((volatile unsigned long *) 0x4002C018))
#define PINSEL7        	(*((volatile unsigned long *) 0x4002C01C))
#define PINSEL8        	(*((volatile unsigned long *) 0x4002C020))
#define PINSEL9        	(*((volatile unsigned long *) 0x4002C024))
#define PINSEL10       	(*((volatile unsigned long *) 0x4002C028))

//GPIOs
#define FIO0DIR        	(*((volatile unsigned long *) 0x2009C000))
#define FIO1DIR        	(*((volatile unsigned long *) 0x2009C020))
#define FIO2DIR        	(*((volatile unsigned long *) 0x2009C040))
#define FIO3DIR        	(*((volatile unsigned long *) 0x2009C060))
#define FIO4DIR        	(*((volatile unsigned long *) 0x2009C080))

#define FIO0PIN        	(*((volatile unsigned long *) 0x2009C014))
#define FIO1PIN        	(*((volatile unsigned long *) 0x2009C034))
#define FIO2PIN        	(*((volatile unsigned long *) 0x2009C054))
#define FIO3PIN        	(*((volatile unsigned long *) 0x2009C074))
#define FIO4PIN        	(*((volatile unsigned long *) 0x2009C094))

#define FIO0SET        	(*((volatile unsigned long *) 0x2009C018))
#define FIO1SET        	(*((volatile unsigned long *) 0x2009C038))
#define FIO2SET        	(*((volatile unsigned long *) 0x2009C058))
#define FIO3SET        	(*((volatile unsigned long *) 0x2009C078))
#define FIO4SET        	(*((volatile unsigned long *) 0x2009C098))

#define FIO0CLR        	(*((volatile unsigned long *) 0x2009C01C))
#define FIO1CLR        	(*((volatile unsigned long *) 0x2009C03C))
#define FIO2CLR        	(*((volatile unsigned long *) 0x2009C05C))
#define FIO3CLR        	(*((volatile unsigned long *) 0x2009C07C))
#define FIO4CLR        	(*((volatile unsigned long *) 0x2009C09C))

//Ethernet
#define MAC1	        (*((volatile unsigned long *) 0x50000000))
#define MAC2	        (*((volatile unsigned long *) 0x50000004))
#define IPGT	        (*((volatile unsigned long *) 0x50000008))
#define IPGR	        (*((volatile unsigned long *) 0x5000000C))
#define CLRT	        (*((volatile unsigned long *) 0x50000010))
#define MAXF	        (*((volatile unsigned long *) 0x50000014))
#define SUPP	        (*((volatile unsigned long *) 0x50000018))
#define IntEnable       (*((volatile unsigned long *) 0x50000FE4))
#define IntClear        (*((volatile unsigned long *) 0x50000FE8))
#define MCMD	        (*((volatile unsigned long *) 0x50000024))
#define MADR	        (*((volatile unsigned long *) 0x50000028))
#define MWTD	        (*((volatile unsigned long *) 0x5000002C))
#define MRDD	        (*((volatile unsigned long *) 0x50000030))
#define MIND	        (*((volatile unsigned long *) 0x50000034))
#define SA0 	        (*((volatile unsigned long *) 0x50000040))
#define SA1 	        (*((volatile unsigned long *) 0x50000044))
#define SA2 	        (*((volatile unsigned long *) 0x50000048))
#define command	        (*((volatile unsigned long *) 0x50000100))
#define STATUS	        (*((volatile unsigned long *) 0x50000104))
#define RxDescriptor    (*((volatile unsigned long *) 0x50000108))
#define RxStatus	   	(*((volatile unsigned long *) 0x5000010C))
#define RxDescNumber    (*((volatile unsigned long *) 0x50000110))
#define RxProIndex	   	(*((volatile unsigned long *) 0x50000114))
#define RxConIndex	  	(*((volatile unsigned long *) 0x50000118))
#define TxDescriptor    (*((volatile unsigned long *) 0x5000011C))
#define TxStatus	   	(*((volatile unsigned long *) 0x50000120))
#define TxDescNumber    (*((volatile unsigned long *) 0x50000124))
#define TxProIndex	   	(*((volatile unsigned long *) 0x50000128))
#define TxConIndex	   	(*((volatile unsigned long *) 0x5000012C))
#define RxFilterCtlr    (*((volatile unsigned long *) 0x50000200))

/* EMAC Memory Buffer configuration for 16K Ethernet RAM. */
#define NUM_RX_FRAG         4           /* Num.of RX Fragments 4*1536= 6.0kB */
#define NUM_TX_FRAG         3           /* Num.of TX Fragments 3*1536= 4.6kB */
#define ETH_FRAG_SIZE       1536        /* Packet Fragment size 1536 Bytes   */

#define ETH_MAX_FLEN        1536        /* Max. Ethernet Frame Size          */

/* EMAC variables located in 16K Ethernet SRAM */
#define RX_DESC_BASE        0x20080000
#define RX_STAT_BASE        (RX_DESC_BASE + NUM_RX_FRAG*8)
#define TX_DESC_BASE        (RX_STAT_BASE + NUM_RX_FRAG*8)
#define TX_STAT_BASE        (TX_DESC_BASE + NUM_TX_FRAG*8)
#define RX_BUF_BASE         (TX_STAT_BASE + NUM_TX_FRAG*4)
#define TX_BUF_BASE         (RX_BUF_BASE  + NUM_RX_FRAG*ETH_FRAG_SIZE)

/* RX and TX descriptor and status definitions. */
#define RX_DESC_PACKET(i)   (*(unsigned int *)(RX_DESC_BASE   + 8*i))
#define RX_DESC_CTRL(i)     (*(unsigned int *)(RX_DESC_BASE+4 + 8*i))
#define RX_STAT_INFO(i)     (*(unsigned int *)(RX_STAT_BASE   + 8*i))
#define RX_STAT_HASHCRC(i)  (*(unsigned int *)(RX_STAT_BASE+4 + 8*i))
#define TX_DESC_PACKET(i)   (*(unsigned int *)(TX_DESC_BASE   + 8*i))
#define TX_DESC_CTRL(i)     (*(unsigned int *)(TX_DESC_BASE+4 + 8*i))
#define TX_STAT_INFO(i)     (*(unsigned int *)(TX_STAT_BASE   + 4*i))
#define RX_BUF(i)           (RX_BUF_BASE + ETH_FRAG_SIZE*i)
#define TX_BUF(i)           (TX_BUF_BASE + ETH_FRAG_SIZE*i)
#define TCTRL_LAST          0x40000000  /* Last Descriptor for TX Frame      */

//UART
#define U0RBR         	(*((volatile unsigned long *) 0x4000C000))
#define U0THR       	(*((volatile unsigned long *) 0x4000C000))
#define U0DLL    	    (*((volatile unsigned long *) 0x4000C000))
#define U0DLM         	(*((volatile unsigned long *) 0x4000C004))
#define U0FCR         	(*((volatile unsigned long *) 0x4000C008))
#define U0LCR         	(*((volatile unsigned long *) 0x4000C00C))
#define U0LSR         	(*((volatile unsigned long *) 0x4000C014))
#define U0FDR         	(*((volatile unsigned long *) 0x4000C028))
#define U0TER         	(*((volatile unsigned long *) 0x4000C030))
#define U0FDR           (*((volatile unsigned long *) 0x4000C028))

//CAN
#define CANTxSR        	(*((volatile unsigned long *) 0x40040000))
#define CANRxSR        	(*((volatile unsigned long *) 0x40040004))
#define CANMSR	        (*((volatile unsigned long *) 0x40040008))


#define CAN1MOD	        (*((volatile unsigned long *) 0x40044000))
#define CAN2MOD	        (*((volatile unsigned long *) 0x40048000))
#define CAN1CMR	        (*((volatile unsigned long *) 0x40044004))
#define CAN2CMR	        (*((volatile unsigned long *) 0x40048004))
#define CAN1GSR	        (*((volatile unsigned long *) 0x40044008))
#define CAN2GSR	        (*((volatile unsigned long *) 0x40048008))
#define CAN1ICR	        (*((volatile unsigned long *) 0x4004400C))
#define CAN2ICR	        (*((volatile unsigned long *) 0x4004800C))
#define CAN1IER	        (*((volatile unsigned long *) 0x40044010))
#define CAN2IER	        (*((volatile unsigned long *) 0x40048010))
#define CAN1BTR	        (*((volatile unsigned long *) 0x40044014))
#define CAN2BTR	        (*((volatile unsigned long *) 0x40048014))
#define CAN1SR	        (*((volatile unsigned long *) 0x4004401C))
#define CAN2SR	        (*((volatile unsigned long *) 0x4004801C))
#define CAN1RFS	        (*((volatile unsigned long *) 0x40044020))
#define CAN2RFS	        (*((volatile unsigned long *) 0x40048020))
#define CAN1RID	        (*((volatile unsigned long *) 0x40044024))
#define CAN2RID	        (*((volatile unsigned long *) 0x40048024))
#define CAN1RDA	        (*((volatile unsigned long *) 0x40044028))
#define CAN2RDA	        (*((volatile unsigned long *) 0x40048028))
#define CAN1RDB	        (*((volatile unsigned long *) 0x4004402C))
#define CAN2RDB	        (*((volatile unsigned long *) 0x4004802C))
#define CAN1TFI1	    (*((volatile unsigned long *) 0x40044030))
#define CAN2TFI1	    (*((volatile unsigned long *) 0x40048030))
#define CAN1TID1	    (*((volatile unsigned long *) 0x40044034))
#define CAN2TID1	    (*((volatile unsigned long *) 0x40048034))
#define CAN1TDA1	    (*((volatile unsigned long *) 0x40044038))
#define CAN2TDA1	    (*((volatile unsigned long *) 0x40048038))
#define CAN1TDB1	    (*((volatile unsigned long *) 0x4004403C))
#define CAN2TDB1	    (*((volatile unsigned long *) 0x4004803C))
#define CAN1TFI2	    (*((volatile unsigned long *) 0x40044040))
#define CAN2TFI2	    (*((volatile unsigned long *) 0x40048040))
#define CAN1TID2	    (*((volatile unsigned long *) 0x40044044))
#define CAN2TID2	    (*((volatile unsigned long *) 0x40048044)) 
#define CAN1TDA2	    (*((volatile unsigned long *) 0x40044048))
#define CAN2TDA2	    (*((volatile unsigned long *) 0x40048048))
#define CAN1TDB2	    (*((volatile unsigned long *) 0x4004404C))
#define CAN2TDB2	    (*((volatile unsigned long *) 0x4004804C))
#define CAN1TFI3	    (*((volatile unsigned long *) 0x40044050))
#define CAN2TFI3	    (*((volatile unsigned long *) 0x40048050))
#define CAN1TID3	    (*((volatile unsigned long *) 0x40044054))
#define CAN2TID3	    (*((volatile unsigned long *) 0x40048054))
#define CAN1TDA3	    (*((volatile unsigned long *) 0x40044058))
#define CAN2TDA3	    (*((volatile unsigned long *) 0x40048058))
#define CAN1TDB3	    (*((volatile unsigned long *) 0x4004405C))
#define CAN2TDB3	    (*((volatile unsigned long *) 0x4004805C))

#define AFMR        	(*((volatile unsigned long *) 0x4003C000))
#define SFF_sa        	(*((volatile unsigned long *) 0x4003C004))
#define SFF_GRP_sa      (*((volatile unsigned long *) 0x4003C008))
#define EFF_sa      	(*((volatile unsigned long *) 0x4003C00C))
#define EFF_GRP_sa      (*((volatile unsigned long *) 0x4003C010))
#define ENDofTable		(*((volatile unsigned long *) 0x4003C014)) 
#define CANAF_RAM_BASE     	0x40038000


//SSP
#define SSP1CR0         (*((volatile unsigned long *) 0x40030000))
#define SSP1CR1         (*((volatile unsigned long *) 0x40030004))
#define SSP1CPSR        (*((volatile unsigned long *) 0x40030010))
#define SSP1DR          (*((volatile unsigned long *) 0x40030008))
#define SSP1SR 			(*((volatile unsigned long *) 0x4003000C))

//PWM
#define PWM1IR         	(*((volatile unsigned long *) 0x40018000))
#define PWM1TCR         (*((volatile unsigned long *) 0x40018004))
#define PWM1TC         	(*((volatile unsigned long *) 0x40018008))
#define PWM1PR         	(*((volatile unsigned long *) 0x4001800C))
#define PWM1PC         	(*((volatile unsigned long *) 0x40018010))
#define PWM1MCR         (*((volatile unsigned long *) 0x40018014))
#define PWM1MR0         (*((volatile unsigned long *) 0x40018018))
#define PWM1MR1         (*((volatile unsigned long *) 0x4001801C))
#define PWM1MR2         (*((volatile unsigned long *) 0x40018020))
#define PWM1MR3         (*((volatile unsigned long *) 0x40018024))
#define PWM1MR4         (*((volatile unsigned long *) 0x40018040))
#define PWM1MR5         (*((volatile unsigned long *) 0x40018044))
#define PWM1MR6         (*((volatile unsigned long *) 0x40018048))
#define PWM1PCR         (*((volatile unsigned long *) 0x4001804C))
#define PWM1LER         (*((volatile unsigned long *) 0x40018050))
#define PWM1CTCR        (*((volatile unsigned long *) 0x40018070))	 

//Power Control Register
#define PCONP           (*((volatile unsigned long *) 0x400FC0C4))

#endif
